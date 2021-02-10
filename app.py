import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR + '/Schedulers')

from flask import Flask
from avery_pill_scheduler import AveryPillScheduler

app = Flask(__name__)

averyPillSched = AveryPillScheduler()

#start scheduled jobs
averyPillSched.avery_pill_job()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
