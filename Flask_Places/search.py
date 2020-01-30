from flask import Flask, redirect, url_for, request, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 
import requests, json

main_URL = 'http://a24b34ec.ngrok.io '
search = Blueprint("search",__name__)

@search.route('/searchbyname')
def searchbyname():
    return render_template("searchbyname.html")

@search.route('/searchbyname', methods=['POST'])
def searchbyname_post():
    name = str(request.form['name'])
    data = {'name':name}
    response = requests.post('http://127.0.0.1:5001'+'/search_place', data = data).json()
    print(response)
    return render_template("searchbynameresponse.html", response = response)