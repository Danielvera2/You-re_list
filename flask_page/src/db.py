from psycopg2 import connect

host = 'localhost'
port = 5432
dbname = 'mistareas'
user = 'postgres'
password = 'Danielvera2003'


psql = connect(host = host, port = port, dbname = dbname, user = user, password = password)