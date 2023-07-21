from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os, psycopg2
from database import load_records_from_db
import pandas as pd

load_dotenv()

app = Flask(__name__)

connection_records = load_records_from_db()

fact_url = 'https://catfact.ninja/fact'

cat_api_key = os.getenv('CAT_API_KEY')

url_search = f"https://api.thecatapi.com/v1/breeds?api_key={cat_api_key}"

@app.route("/")
def index():
    """
    for i in CAT_LOC:
        if str(cat_code_data) in i['country']:
            url_lat_lon_list = list(i['latitude'], i['longitude'])

            for i in {{ brython_table_db }}:
                if cat_facts_dict["country_code"] in i['country']:
                    lat, long, country, name = i['latitude'], i['longitude'], i['country'], i['name']

    """
    return render_template('index.html', brython_cat_breeds = url_search, brython_fact_url = fact_url
)

@app.route("/api/country", methods=["GET"])
def get_all_users():
    if connection_records:
        result = []
        for record in connection_records:
            result.append({
                'country': record[0],
                'latitude': record[1],
                'longitude': record[2],
                'name': record[3]})        
        return jsonify(result)
    else:
        return jsonify({"error": f"country not found."}), 404          

if __name__ == '__main__':
    app.run()