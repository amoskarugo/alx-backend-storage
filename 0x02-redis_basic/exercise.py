#!/usr/bin/env python3
"""redis basics"""
import redis
import uuid
from typing import Callable, Optional, Union


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(f"{key}")

        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''
            Get a string from the cache.
        '''
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        '''
            Get an int from the cache.
        '''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
