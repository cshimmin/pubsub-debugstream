#!/usr/bin/env python
'''
Simple debug program that listens to everything on the debug stream
'''

import redis
import cPickle

if __name__ == "__main__":
    # connect to redis
    rdb = redis.StrictRedis()

    pubsub = rdb.pubsub()
    pubsub.psubscribe('debug_stream:*')
    print "listening for published messages..."
    for pubmsg in pubsub.listen():
        if not pubmsg['type'].endswith('message'): continue

        # unpack the payload
        msg = cPickle.loads(pubmsg['data'])

        # print some info
        print "Sender: %s\trand: %0.4f" % (msg['uid'], msg['random_number'])
