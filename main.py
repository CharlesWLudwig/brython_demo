from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

fact_url = 'https://catfact.ninja/fact'

cat_api_key = os.getenv('CAT_API_KEY')

url_search = f"https://api.thecatapi.com/v1/breeds?api_key={cat_api_key}"

@app.route("/")
def index():
    return render_template('index.html', brython_cat_breeds = url_search, brython_fact_url = fact_url)

if __name__ == '__main__':
    app.run(debug=True, port=5002, use_reloader=True)