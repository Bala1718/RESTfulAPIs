from flask import Flask

app = Flask(__name__)


@app.route('/players')
def playersFunction():
    return "List of Players!"


@app.route('/players/<int:id>')
def playersFunctionId(id):
    return "Return Players Name"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
