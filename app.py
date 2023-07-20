from flask import Flask, render_template, request
from dotenv import load_dotenv
import os, psycopg2
from database import load_records_from_db

load_dotenv()

app = Flask(__name__)

connection_records = load_records_from_db()

CAT_LOC = []

for record in connection_records:
    CAT_LOC.append({
        'country': record[0],
        'latitude': record[1],
        'longitude': record[2],
        'name': record[3],
})

fact_url = 'https://catfact.ninja/fact'

cat_api_key = os.getenv('CAT_API_KEY')

url_search = f"https://api.thecatapi.com/v1/breeds?api_key={cat_api_key}"

@app.route("/")
def index():
    cat_code_data = request.args.get("cat_code")

    for i in CAT_LOC:
        if str(cat_code_data) in i['country']:
            print(i['latitude'], i['longitude'])

    return render_template('index.html', brython_cat_breeds = url_search, brython_fact_url = fact_url,
    url_lat = cat_code_data,
    url_lon = cat_code_data
)

if __name__ == '__main__':
    app.run()