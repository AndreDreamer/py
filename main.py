from waitress import serve
from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/hello-world-24')
def index():
    return "Hello World 24"


if __name__ == '__main__':
    serve(app)
