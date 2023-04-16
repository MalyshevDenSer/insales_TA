import redis
import pickle
import models
from settings import CACHE_TIME_TO_LIVE

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def get_game_query(db):
    key = 'games_cache'
    if redis_client.exists(key):
        result = pickle.loads(redis_client.get(key))
    else:
        result = db.query(models.Game).filter().first()
        redis_client.set(key, pickle.dumps(result), CACHE_TIME_TO_LIVE)
    return result


def update_cache(db):
    key = 'games_cache'
    result = db.query(models.Game).filter().first()
    redis_client.set(key, pickle.dumps(result), CACHE_TIME_TO_LIVE)
