from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp', methods = ['POST', 'GET'])

def weatherapp():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {
        'q': request.form.get('city'),
        'appid': request.form.get('appid'),
        'units': request.form.get('units')
    }

    response = requests.get(url, params=param)
    data = response.json()
    return f'data : {data}'

if __name__ == '__main__':
    app.run(debug = True, port = 8002)



