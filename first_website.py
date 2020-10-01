#!/usr/bin/env python
# -*- coding: latin-1 -*-

from flask import Flask, render_template, request

# __name__ ist der Eigenname der Datei also "first_website_server.py". Theoretisch könnnen ja auch externe Module gelesen werden. 
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("startseite.html")

@app.route("/test")
def test():
    args = request.args
    name = request.args.get("name")
    alter = request.args.get("age")
    if name != None and alter != None:
        print (name + " ist " + alter + " Jahre alt.")
    return render_template("test.html", name= name)

@app.route("/formular")
def formular():
    name = request.args.get("name")
    alter = request.args.get("age")
    print (name, alter)
    return render_template("formular.html", name = name, age = alter)


if __name__ == '__main__':
    app.run(debug=True)