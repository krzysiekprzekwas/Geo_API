postgresql = {'host': 'ec2-34-248-148-63.eu-west-1.compute.amazonaws.com',
         'user': 'vvxvykgemntkhb',
         'passwd': '563eebc36fbbf9fc68c632b89927f9146a5707bf1b77bb8cd2b35078ea92c5c5',
         'db': 'dafbf7r9lf2dto'}

ipstack_API_ADRESS = 'http://api.ipstack.com/'
ipstack_API_KEY = 'c01e741afebed7e5eab4dbb1a07223b8'

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])

