DOMAIN = {'article': {}}

MONGO_HOST = 'ds025973.mlab.com'
MONGO_PORT = 25973

# Skip these if your db has no auth. But it really should.
# MONGO_USERNAME = 'admin'
# MONGO_PASSWORD = 'aggregio'

MONGO_DBNAME = 'aggregio-test'

MONGO_QUERY_BLACKLIST = ['$where']