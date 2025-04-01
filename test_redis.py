import numpy as np
import redis
import redis.connection

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('erfan', 'bayat')
print(r.get('erfan').decode())