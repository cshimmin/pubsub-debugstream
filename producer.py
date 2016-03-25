#!/usr/bin/env python

import random
import redis
import time
import cPickle

IDs = ['chase', 'jared', 'herschel', 'hypatia', 'gene_simmons']

if __name__ == "__main__":
    # connect to redis
    rdb = redis.StrictRedis()

    serial = 0
    while True:
        # make some phoney data and pack it into a pkl
        uid = random.choice(IDs)
        serial += 1

        payload = cPickle.dumps({
            'uid': uid,
            'serial': serial,
            'random_number': random.random(),
            })

        # put the data on the (right side of the) queue
        rdb.rpush('msg_queue', payload)

        print "posted message %d from %s" % (serial, uid)

        # sleep a bit
        time.sleep(0.1+random.random()*1.4)
