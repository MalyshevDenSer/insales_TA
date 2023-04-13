import redis
import pickle
import models

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def get_game_guery(db):
    key = 'games_cache'
    if redis_client.exists(key):
        result = pickle.loads(redis_client.get(key))
    else:
        result = db.query(models.Game).filter().first().__dict__
        result.pop('_sa_instance_state')
        redis_client.set(key, pickle.dumps(result))
    return result


def update_cache(db):
    key = 'games_cache'
    result = db.query(models.Game).filter().first()
    redis_client.set(key, pickle.dumps(result))
