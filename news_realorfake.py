import joblib
import pandas as pd

def newsaccuracy(title, text):
    model = joblib.load('news_realorfake.pkl')
    combined_text = title + ' ' + text

    vectorizer = joblib.load('tfidvec.pkl')
    input = vectorizer.transform([combined_text])

    y_pred = model.predict(input)

    return y_pred
