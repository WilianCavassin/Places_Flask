from flask import Flask, redirect, url_for, request, Blueprint, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from werkzeug.utils import secure_filename
import os
import requests
# convert address to lat long
from geopy.geocoders import Nominatim

main_URL = 'http://a24b34ec.ngrok.io'
places = Blueprint("places", __name__)



#converts address to lat long
def geocode(address):
    geo_locator = Nominatim()
    try:
        location = geo_locator.geocode(address)
    except:
        return render_template("viewspots.html")
    return location

# return page for search
@places.route('/viewspots')
def viewspots():
    return render_template("viewspots.html")

@places.route('/viewspots', methods=['POST'])
def viewspots_post():
    return ('to-do')