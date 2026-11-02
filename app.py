from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to PythonanyWhere!"

@app.route('/hello')
def hello():
    return "hello Students1"

if __name__ == '__main__:
    app.run(debug=True)