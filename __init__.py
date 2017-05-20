from flask import Flask, send_file, render_template
from mysql import *
from settings import db_config
import itertools
import json

app = Flask(__name__)


"""Get the database Details"""
db = MySQLDatabase(db_config.get('db_name'),
                   db_config.get('user'),
                   db_config.get('pass'),
                   db_config.get('host'))

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/userStats')
def userStats():
    return render_template('userStats.html')#, activeUsers = searchDB())

@app.route('/dash/projects')
def dash_project():
    #result = searchDB()
    result = searchDB()
    #print result
    return json.dumps(list(result))

@app.route('/testPage')
def testPage():
    return render_template('testPage.html', tables = [val for sublist in list(db.get_available_tables()) for val in sublist])#, columns = db.get_columns_for_table())

if __name__ == "__main__":
    app.run(host='127.0.0.1')

#[val for sublist in db.get_available_tables() for val in sublist]