import redis
import pickle
import models

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def get_game_query(db):
    key = 'games_cache'
    if redis_client.exists(key):
        print('GET FROM CACHE')
        result = pickle.loads(redis_client.get(key))
    else:
        print('CACHING')
        result = db.query(models.Game).filter().first()
        redis_client.set(key, pickle.dumps(result), 5)
    return result


def update_cache(db):
    print('UPDATING CACHE')
    key = 'games_cache'
    result = db.query(models.Game).filter().first()
    redis_client.set(key, pickle.dumps(result), 5)
