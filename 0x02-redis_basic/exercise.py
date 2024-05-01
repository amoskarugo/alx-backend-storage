#!/usr/bin/env python3
"""redis basics"""
import redis
import uuid


class Cache:
    """
        Cache class the instantiates an instance of Redis class
    """
    def __init__(self) -> None:
        """
            Initialize a new instance of the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> any:
        """method to set a value in redisdb"""
        key = str(uuid.uuid4())

        self._redis.set(f"{key}", data)
        return key
