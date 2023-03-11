from flask import Flask
from visa.logger import logging

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    logging.info('We are just testing logging module in flask app.')
    return 'flask app with logger'


if __name__ == '__main__':
    app.run(debug=True)

