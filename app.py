from flask import Flask
import config.old_calendar.old_calendar_api as old
import json

app = Flask(__name__)
app.debug = True
old_ret = old.get_old_calendar()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/old')
def old():
    return json.dumps(old_ret)
    # if request.method == "GET":
    #     old_ret = old.get_old_calendar()
    #     return json.dumps(old_ret)
    # else:
    #     return "API ERROR"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
