import os
import psycopg2
from flask import Flask, current_app, g

def get_db():
    if 'db' not in g:
        url = 'postgresql://{username}@{host}/{database}'.format(
            username='postgres',
            host=current_app.config['DATABASE_HOST'],
            database='flard_app',
        )
        g.db = psycopg2.connect(url)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
app = Flask(__name__)
app.config['DATABASE_HOST'] = os.environ.get('DATABASE_HOST', 'localhost')

@app.route('/')
def hello_world():
    return {'status': 'success'}

@app.route('/db')
def db():
    with get_db() as connection:
        with connection.cursor() as cursor:
            sql = 'select * from customers'
            cursor.execute(sql)
            rows = cursor.fetchall()
    return {
        'data': rows,
    }

@app.route('/test')
def test():
    return {
        'data': 'test',
    }

