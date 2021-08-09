import os
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
soup = BeautifulSoup(html_source, 'html.parser')


@app.route('/')
def index():
    analysis_url = "https://github.com/topics/data-analysis"
    machine_learning_url = 'https://github.com/topics/machine-learning'
    analysis_response = requests.get(analysis_url)
    machine_learning_response = requests.get(machine_learning_url)
    analysis_content = analysis_response.text
    machine_learning_content = machine_learning_response.text
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
