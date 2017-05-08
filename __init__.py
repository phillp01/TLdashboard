from flask import Flask, send_file, render_template
from mysql import searchDB
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/userStats')
def userStats():
    return render_template('userStats.html', activeUsers = searchDB())

@app.route('/dash/projects')
def dash_project():
    #result = searchDB()
    result = searchDB()

    print result
    return json.dumps(list(result))

if __name__ == "__main__":
    app.run(host='127.0.0.1')

