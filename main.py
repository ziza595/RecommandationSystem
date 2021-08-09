import os
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)



@app.route('/')
def index():
    analysis_url = "https://github.com/topics/data-analysis"
    machine_learning_url = 'https://github.com/topics/machine-learning'
    analysis_response = requests.get(analysis_url)
    machine_learning_response = requests.get(machine_learning_url)
    analysis_content = analysis_response.text
    machine_learning_content = machine_learning_response.text
    soup_analysis = BeautifulSoup(analysis_content, 'html.parser')
    soup_machine_learning = BeautifulSoup(machine_learning_content, 'html.parser')
    return render_template(
        'index.html',
        analysis_url=analysis_url,
        machine_learning_url=machine_learning_url,
        analysis_response=analysis_response,
        machine_learning_response=machine_learning_response,
        analysis_content=analysis_content
        machine_learning_content=machine_learning_content
        soup_analysis=soup_analysis
        soup_machine_learning=soup_machine_learning
    )


if __name__ == '__main__':
    app.run(debug=True)
