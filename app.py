from flask import Flask, render_template
from dotenv import load_dotenv
import os, psycopg2
from database import load_records_from_db

load_dotenv()

app = Flask(__name__)

connection_records = load_records_from_db()

CAT_LOC = []

for record in connection_records:
    CAT_LOC.append({
        'post_code': record[0],
        'country': record[1],
        'country_abbreviation': record[2],
        'place_name': record[3],
        'longitude': record[4],
        'us_state': record[5],
        'state_abbreviation': record[6],
        'latitude': record[7],
})
    
fact_url = 'https://catfact.ninja/fact'

cat_api_key = os.getenv('CAT_API_KEY')

url_search = f"https://api.thecatapi.com/v1/breeds?api_key={cat_api_key}"

@app.route("/")
def index():
    return render_template('index.html', brython_cat_breeds = url_search, brython_fact_url = fact_url,
    cat_table_db = CAT_LOC
)

if __name__ == '__main__':
    app.run()