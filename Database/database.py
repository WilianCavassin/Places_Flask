from flask import Flask, request, jsonify, Blueprint, render_template, redirect, url_for, request, flash
import requests
import os
import flask_login
import sqlite3
import json
main_URL = 'http://127.0.0.1/5001'
app = Flask(__name__)
app.secret_key = 'secret2'

#LATER->BUILD LOG TO RESTORE!!!
#in->data from place
#out->ok if process sucees none if some error

@app.route('/regplace', methods=['POST'])
def regplace():
    conn = sqlite3.connect('../Flask_Places/db.sqlite3')
    #get data from the post
    name = str(request.form['name'])
    lat = float(request.form['lat'])
    lon = float(request.form['lon'])
    id_user = int(request.form['id_user'])
    category = str(request.form['category'])
    country = str(request.form['country'])
    image = str(request.form['file'])

    #check if category already exist, improve security
    cur = conn.cursor()
    cur.execute("SELECT id, name from categories where name = '%s'" % category)
    print(name)
    print(cur)
    if cur.fetchone() == None:
        cur.execute("INSERT INTO categories VALUES (NULL,'%s')" % category)
        conn.commit()
    cur.execute("SELECT id, name from categories where name = '%s'" % category)
    print(cur)
    #search, convert, store
    rows = cur.fetchall()
    for row in rows:
        cat_id = int(row[0])
    print(cat_id)
    #store in places
    places_insert = (name, lat, lon, id_user, cat_id, country)
    cur.execute("INSERT INTO places(name, lat, lon, id_user, category, country) VALUES (?, ?, ?, ?, ? ,?)", places_insert)
    conn.commit()
    #get place id
    cur.execute("SELECT id, name from places where name = '%s'" % name)
    places = cur.fetchall()
    for place in places:
        place_id = int(place[0])
    #store in images
    image_insert = (place_id, id_user, image)
    cur.execute("INSERT INTO places_images(id_place, id_user, image) VALUES (?, ?, ?)", image_insert)
    conn.commit()
    return ('ok')    

@app.route('/search_place', methods=['POST'])
def search_place():
    conn = sqlite3.connect('../Flask_Places/db.sqlite3')
    cur = conn.cursor()
    name = str(request.form['name'])
    cur.execute("SELECT id, name, lat, lon, category, votes, country from places where name = '%s'" %name)
    places = json.dumps(cur.fetchall())
    print(places)
    return places
    #for place in places:

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5001, debug=True)