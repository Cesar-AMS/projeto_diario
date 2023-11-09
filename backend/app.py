from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/frontend/templates/index.html')
def serve_index():
    return send_from_directory('frontend', 'templates', 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
