#!/usr/bin/env python

import redis
import cPickle

if __name__ == "__main__":
    # connect to redis
    rdb = redis.StrictRedis()

    while True:
        # pop data off the (left side of the) queue, blocking if necessary
        _, msg_pkl = rdb.blpop('msg_queue')

        # un-pickle the message
        msg = cPickle.loads(msg_pkl)
        
        # check the sender:
        sender = msg['uid']
        print "got message %d from %s" % (msg['serial'], sender)

        # check redis to see see if the sender is
        # listed in the debug stream
        if rdb.sismember('debug_stream:IDs', sender):
            # post message to the debug stream
            nclient = rdb.publish('debug_stream:%s'%sender, msg_pkl)
            print "%s is in the debug stream! published to %d clients." % (sender, nclient)
