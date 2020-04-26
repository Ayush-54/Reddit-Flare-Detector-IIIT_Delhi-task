import praw
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)
app.config['client_secret'] = 'Sn1bZ2ID-P5X6hFV-mjt09v0j5c'
app.config['client_id'] = 'NVyf-I0I6atu2w'
app.config['user_agent'] = 'Testing_api'
app.config['username'] = 'reddit_testbyayush'
app.config['password'] = 'password'
#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

def Flair_Predictor(url):
    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    result = loaded_model.predict([url])
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    url = index()
    result = Flair_Predictor(url)
        
    return render_template("result.html", result=result)

