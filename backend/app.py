from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Inicial'


@app.route('/sobre')
def about():
    return 'Sobre Nós'


if __name__ == '__main__':
    app.run()
