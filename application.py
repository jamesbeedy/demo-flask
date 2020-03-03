#!/usr/bin/env python3

from flask import Flask
import logging, logging.config, yaml


yaml.warnings({'YAMLLoadWarning': False})
logging.config.dictConfig(yaml.load(open('logging.yaml')))


logfile    = logging.getLogger('file')
logconsole = logging.getLogger('console')



app = Flask(__name__)


@app.route('/test')
def test_pass():
    logfile.debug("TEST")
    logconsole.debug("TEST")
    return "TEST"



@app.route("/error")
def error():
    logfile.error("ERROR")
    logconsole.error("ERROR")
    return "a" / 2


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
