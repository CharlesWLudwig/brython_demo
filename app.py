from flask import Flask, render_template
from dotenv import load_dotenv
import os, psycopg2

load_dotenv()

app = Flask(__name__)

fact_url = 'https://catfact.ninja/fact'

cat_api_key = os.getenv('CAT_API_KEY')

url_search = f"https://api.thecatapi.com/v1/breeds?api_key={cat_api_key}"

def connect_to_postgres():
    try:
        conn = psycopg2.connect(os.getenv('POSTGRES_URL'))

        print('Connecting to the PostgreSQL database...')
            
        cur = conn.cursor()
        
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

@app.route("/")
def index():
    return render_template('index.html', brython_cat_breeds = url_search, brython_fact_url = fact_url, postgres_connection=connect_to_postgres())

#if __name__ == '__main__':
#    app.run()