# Import relevant packages
from flask import Flask, jsonify, redirect, url_for, render_template
import csv
import os
import pandas
# Create an instance of our app
app = Flask(__name__)



# localhost:5000 this is the default port for Flask
# @app.route("/")
# def login():
#     return render_template("home.html")



@app.route('/')
def jobs():
    filename = '/home/vagrant/ItJobsWatchTop30.csv'
    data = pandas.read_csv(filename, header=0)
    joblist = list(data.values)
    return render_template('home.html', joblist=joblist)



if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
