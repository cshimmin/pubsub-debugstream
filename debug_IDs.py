#!/usr/bin/env python

import redis

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Add/remove IDs from the debug stream")
    parser.add_argument("--add", metavar="ID", nargs="+", default=[], help="add ID(s) to the debug stream.")
    parser.add_argument("--remove", metavar="ID", nargs="+", default=[], help="remove ID(s) from the debug stream.")
    args = parser.parse_args()

    # connect to redis
    rdb = redis.StrictRedis()

    for i in args.add:
        print "Adding", i
        rdb.sadd('debug_stream:IDs', i)
    for i in args.remove:
        print "Removing", i
        rdb.srem('debug_stream:IDs', i)
