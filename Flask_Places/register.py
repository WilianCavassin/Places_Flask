from flask import Flask, redirect, url_for, request, Blueprint, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from werkzeug.utils import secure_filename
import os
import requests
import re

# convert address to lat long
from geopy.geocoders import Nominatim

main_URL = 'http://a24b34ec.ngrok.io'
register = Blueprint("register",__name__)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#converts address to lat long
def geocode(address):
    geo_locator = Nominatim()
    try:
        location = geo_locator.geocode(address)
    except:
        return render_template("registerspots.html")
    return location

@register.route('/registerspots')
def registerspots():
    return render_template("registerspots.html")

@register.route('/registerspots', methods=['POST'])
def registerspots_post():
    # check if the post request has the file part
    if 'file' not in request.files:
        return render_template('viewspots.html')
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return render_template('viewspots.html')
    # define path and join with the filename
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        fileway = os.getcwd()+('\Flask_Places\static\images')
        #verify if the file exists, if so add 1 after it
        filecompose = os.path.normpath(os.path.join(fileway, filename))
        while os.path.exists(filecompose):
            filecompose = filecompose+'1'
        file.save(filecompose)
    name = str(request.form['name'])
    street = str(request.form['street'])
    number = str(request.form['number'])
    city = str(request.form['city'])
    state = str(request.form['state'])
    country = str(request.form['country'])
    print(country)
    address = street+', '+number+', '+city+', '+state+', '+country
    print(address)
    coord = geocode(address)
    data = {'name':str(request.form['name']), 
        'lat': coord.latitude, 
        'lon': coord.longitude, 
        'id_user': current_user.id,
        'category': str(request.form['category']),
        'country': country,
        'file': filecompose} 
    #localhost // different port
    response = str(requests.post('http://127.0.0.1:5001'+'/regplace', data = data).content)
    r = re.findall(r"'(.*?)'",response)[0]
    print(r)
    if r=='ok':
        flash(name+'is registered')
        return render_template('profile.html')
    elif r==None:
        flash("Connection Error, contact support")
        return render_template("registerspots.html")
    else:
        flash(name+'is not registered, contact support.')
        return render_template('profile.html')
