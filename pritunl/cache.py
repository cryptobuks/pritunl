from pritunl.helpers import *
from pritunl.constants import *
from pritunl import settings

import redis

_client = None
has_cache = False

def init():
    global _client
    global has_cache

    redis_uri = settings.app.redis_uri
    if not redis_uri:
        return

    has_cache = True
    _client = redis.StrictRedis.from_url(
        redis_uri,
        socket_timeout=settings.app.redis_timeout,
        socket_connect_timeout=settings.app.redis_timeout,
    )

def get(key):
    return _client.get(key)

def set(key, val):
    return _client.set(key, val)

def setex(key, ttl, val):
    return _client.setex(key, ttl, val)

def lpush(key, *vals):
    return _client.lpush(key, *vals)

def lpushc(key, cap, *vals):
    _client.lpush(key, *vals)
    return _client.ltrim(key, cap)

def rpush(key, *vals):
    return _client.rpush(key, *vals)

def push(key, *vals):
    return _client.lpush(key, *vals)

def remove(key):
    return  _client.delete(key)