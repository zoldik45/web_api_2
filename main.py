from flask import redirect, Flask, request, render_template, jsonify, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import webbrowser



app = Flask(__name__)
adminpasswod = "admin"
adminlogin = "admin"
@app.route('/')
@app.route('/index')
def index():
        return "Привет, Яндекс!"

@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
<!-- Coding By CodingNepal - codingnepalweb.com -->
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Login & Signup Form</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" />
</head>
<body>
  <section class="wrapper">
    <div class="form signup">
      <header>Admin Login</header>
      <form method="post" id="signupForm">
        <input type="text" placeholder="Full_name" name="Full_name" id="signupFullName" required />
        <input type="password" placeholder="Password" name="Password" id="signupPassword" required />
        <input type="submit" value="Sign in" />
      </form>
</div>'''
    elif request.method == 'POST':
        a = request.form['Full_name']
        b = request.form['Password']
        if a == adminlogin and b == adminpasswod:
            return webbrowser.open("https://korporativnoepitanie.tb.ru/catalog")
        else:
            return "ошибка регистрации"





if __name__ == "__main__":
    app.run(debug=True)

