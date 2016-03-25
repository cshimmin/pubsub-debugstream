#!/usr/bin/env python
'''
Another simple debug program that listens to only a particular ID on the debug stream.
'''

import redis
import cPickle
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print >>sys.stderr, "please tell me who to listen to!"
        sys.exit(1)

    uid = sys.argv[1]

    # connect to redis
    rdb = redis.StrictRedis()

    pubsub = rdb.pubsub()
    pubsub.subscribe('debug_stream:%s'%uid)
    print "listening for published messages by %s..." % uid
    for pubmsg in pubsub.listen():
        if not pubmsg['type'].endswith('message'): continue

        # unpack the payload
        msg = cPickle.loads(pubmsg['data'])

        # print some info
        print "Sender: %s\trand: %0.4f" % (msg['uid'], msg['random_number'])
