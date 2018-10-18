from flask import Flask
app = Flask(__name__)

@app.route('/about')
def hello_world():
    return 'Hello World!'

@app.route('/contact/<name>')
def about(name):
    return 'TRYRM has ' + name + '!'

if __name__ == '__main__':
  app.run(host='0.0.0.0')


