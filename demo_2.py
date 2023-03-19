import sys

from flask import Flask, make_response

from visa.exception import CustomException
from visa.logger import logging

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        resp = make_response('Hello World!')
        raise Exception('We are testing custom exception')
    except Exception as e:
        visa = CustomException(e, sys)
        logging.info(visa.error_message)
        logging.info("We are testing logging file")

    return resp


if __name__ == "__main__":
    app.run(debug=True)
