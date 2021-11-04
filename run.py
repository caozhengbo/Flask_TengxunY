from config import load_config
from flask import Flask
from flask import render_template
import config.old_calendar.old_calendar_api as old
import json

app = Flask(__name__)
config = load_config()
app.config.from_object(config)
app.debug = True


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/old')
def old_calendar():
    old_ret = old.get_old_calendar()
    return old_ret


if __name__ == '__main__':
    app.run()
