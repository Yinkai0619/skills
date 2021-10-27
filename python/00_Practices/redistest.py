#!/usr/bin/env python

import redis
import time

pool = redis.ConnectionPool(host="localhost", port=6379, password="redispass", db=20)
r = redis.Redis(connection_pool=pool)
# r.flushdb
for i in range(1000):
    r.set("k%d" % i, "v%d" % i)
    data=r.get("k%d" % i)
    print(data)
# print(r.keys)
