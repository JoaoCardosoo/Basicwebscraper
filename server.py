from flask import Flask, render_template, request
from views import views
import requests
import pprint
import json

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

api = "291607784bdc4dfc97736f907a87eea8"
url = 'https://newsapi.org/v2/top-headlines?q=trump&apiKey=291607784bdc4dfc97736f907a87eea8'

params = {
    'country': 'us',
    'apiKey': '291607784bdc4dfc97736f907a87eea8',
    'category': 'general'
}

@app.route('/', methods=['GET', 'POST'])
def search():
    articles = []
    if request.method == 'POST':
        query = request.form.get('query')
        if query == 'top':
            response = requests.get(url, params=params)
            response_json = response.json()
            return render_template('index.html', results=response_json)
        print ('Author:' + response_json['Author'])
    return render_template('index.html', articles=articles)         

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
