from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'country_timezones.json')
    with open(json_path) as f:
        countries = json.load(f)
    return render_template("index.html", countries=countries)

if __name__ == '__main__':
    app.run(debug=True)
