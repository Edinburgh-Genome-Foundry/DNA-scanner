from flask import Flask
import sys
import optparse
import time
from Controller.app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

from Controller import routes
