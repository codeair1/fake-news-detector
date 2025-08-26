from news_realorfake import newsaccuracy
from flask import Flask,request,jsonify,render_template
import pandas as pd

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    title = request.form['title']
    text = request.form['text']

    output = newsaccuracy(title,text)
    return render_template('index.html',prediction_text = f'the news is detected to be:  {output[0]}')

if __name__ == "__main__":
    app.run(debug=False)
