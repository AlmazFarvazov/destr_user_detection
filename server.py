from flask import Flask, render_template, request
import requests
from mock_predict import predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {}
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            data = predict(url)
        except requests.exceptions.RequestException as e:
            data = str(e)
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
