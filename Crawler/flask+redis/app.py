from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    useragent = request.headers.get('User-agent')
    return '<h1>your browser is %s<h1>' % useragent , 400

@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s<h1>' % name

if __name__ == '__main__':
    app.run(debug=True)