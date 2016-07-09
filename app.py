from eve import Eve
import redis

r = redis.StrictRedis(host='pub-redis-11957.us-east-1-3.4.ec2.garantiadata.com', port=11957, db=0)

app = Eve(redis=r)

if __name__ == '__main__':
    app.run()