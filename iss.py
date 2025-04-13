import requests
import json
import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def iss():
    while(True): 

        response = requests.get('http://api.open-notify.org/iss-now.json')
        raw_data = response.text
        parsed_data = json.loads(raw_data)

        longitude = parsed_data['iss_position']['longitude']
        latitude = parsed_data['iss_position']['latitude']

        time.sleep(5)

        return render_template('coordinates.html', x=longitude, y=latitude)
