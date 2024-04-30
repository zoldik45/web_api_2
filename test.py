import sqlite3

from flask import Flask, url_for
from flask import request
from flask import render_template
import webbrowser


app = Flask(__name__)
adminpasswod = "admin"
adminlogin = "admin"

@app.route('/')
@app.route('/index')
def index():
        return "Привет, Яндекс!"




@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        # Ниже HTML-строка возвращается прямо внутри функции
        return '''<!DOCTYPE html>
<html>
<head>
  <title>Добавление нового блюда в каталог блюд</title>
  <style>
    body {
      background-color: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
    }

    h1 {
      color: white;
      font-size: 24px;
      text-align: center;
      margin-bottom: 20px;
    }

    .form-container {
      background-color: black;
      padding: 20px;
      border-radius: 10px;
      width: 400px;
      text-align: center;
    }

    label, input, textarea {
      display: block;
      margin-bottom: 10px;
      color: white;
      text-align: left;
    }

    input[type="text"], input[type="number"], textarea {
      width: 100%;
      color: black;
      padding: 6px;
    }

    input[type="submit"] {
      background-color: #dec311;
      color: black;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1><strong>Добавление нового блюда в каталог блюд</strong></h1>
    <form method="post" action="/form_sample"> <!-- Добавлен атрибут method POST -->
      <label for="dishName">Введите название блюда:</label>
      <input type="text" id="dishName" name="dishName" required>

      <label for="dishDescription">Введите описание блюда:</label>
      <textarea id="dishDescription" name="dishDescription" required></textarea>

      <label for="dishPrice">Цена:</label>
      <input type="number" id="dishPrice" name="dishPrice" required>

      <input type="submit" value="Добавить в базу данных">
      <button onclick="location.href='https://www.example.com';">Настроить бизнес ланч</button>

    </form>
  </div>
</body>
</html>'''
    elif request.method == 'POST':
        c = request.form['dishName']
        d = request.form['dishDescription']
        e = request.form['dishPrice']
        with sqlite3.connect('bluda.db') as db:
            cursor = db.cursor()
            query_1 = """INSERT INTO eda (name, opisanie, cena) VALUES (?, ?, ?)"""
            cursor.execute(query_1, (c, d, e))  # Использование параметров запроса
            db.commit()
        print(c, d, e)
        return webbrowser.open_new_tab('http://127.0.0.1:8080//form_sample')

@app.route('/register', methods=['POST', 'GET'])
def adminreg():
    if request.method == 'GET':
        # Ниже HTML-строка возвращается прямо внутри функции
        return '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Регистрация пользователя</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .registration-form {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box; /* Added box-sizing */
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            border: none;
            background-color: #c7ad04;
            color: white;
            text-transform: uppercase;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #4cae4c;
        }
        .registration-form h2 {
            text-align: center;
            margin: 0 0 15px;
        }
    </style>
</head>
<body>
    <div class="registration-form">
        <h2>Регистрация</h2>
        <form action="/register" method="post">
            <input type="text" name="username" placeholder="Логин" required>
            <input type="password" name="password" placeholder="Пароль" required>
            <input type="submit" value="Зарегистрироваться">
        </form>
    </div>
</body>
</html>
        '''
    elif request.method == 'POST':
        u = request.form['username']
        o = request.form['password']
        with sqlite3.connect('admini.db') as db:
            cursor = db.cursor()
            query_1 = """INSERT INTO admini (login, parol) VALUES (?, ?)"""
            cursor.execute(query_1, (u, o))  # Использование параметров запроса
            db.commit()
        return webbrowser.open_new_tab('https://korporativnoepitanie.tb.ru')

@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login & Signup Form</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  <style>
    body {
      background-color: #f3f3f3;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }

    .form-wrapper {
      background-color: #ffffff;
      padding: 40px;
      border-radius: 5px;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }

    .form-header {
      text-align: center;
      font-size: 24px;
      color: #333333;
      margin-bottom: 20px;
    }

    .form-input {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #dddddd;
      border-radius: 4px;
    }

    .form-submit {
      width: 100%;
      padding: 10px;
      background-color: #c7ad04;
      color: #ffffff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .form-submit:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-wrapper">
    <h2 class="form-header">Авторизация</h2>
    <form method="post" id="signupForm">
      <input type="text" placeholder="login" name="Full_name" class="form-input" required>
      <input type="password" placeholder="Password" name="Password" class="form-input" required>
      <input type="submit" value="Войти" class="form-submit">
    </form>
  </div>
</body>
</html>'''
    elif request.method == 'POST':
        a = request.form['Full_name']
        b = request.form['Password']
        print(a, b)
        # Соединение с базой данных
        conn = sqlite3.connect('admini.db')
        cursor = conn.cursor()

        # Формирование SQL-запроса
        query = "SELECT * FROM admini WHERE login=? AND parol=?"

        # Выполнение запроса с подстановкой переменных a и b
        cursor.execute(query, (a, b))

        # Получение первой записи из курсора (если запрос вернул результат)
        record = cursor.fetchone()

        # Закрытие соединения с базой данных
        conn.close()

        # Проверка, есть ли запись в базе данных
        if record:
            return '''<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
  <title>Добавление нового блюда в каталог блюд</title>
  <style>
    body {
      background-color: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
    }

    h1 {
      color: #2d0909;
      font-size: 24px;
      text-align: center;
      margin-bottom: 20px;
    }

    .form-container {
      background-color: #ffffff;
      padding: 25px;
      border-radius: 13px;
      width: 500px;
      text-align: center;
    }

    label, input, textarea {
      display: block;
      margin-bottom: 10px;
      color: black;
      text-align: left;
    }

    input[type="text"], input[type="number"], textarea {
      width: calc(100% - 16px); /* Adjusted width to account for padding */
      color: black;
      padding: 8px;
      margin-bottom: 20px;
    }

    .buttons-container {
      display: flex;
      justify-content: space-evenly; /* Distributes space evenly between the buttons */
      padding: 10px 0;
    }

    .button {
      background-color: #048fda;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      cursor: pointer;
      outline: none;
    }

    .button:nth-child(2) {
      background-color: #048fda; /* A different color for the second button */
    }

  </style>
</head>
<body>
  <div class="form-container">
    <h1><strong>Добавление нового блюда в каталог блюд</strong></h1>
    <form method="post" action="/form_sample" id="dishForm">
      <label for="dishName">Введите название блюда:</label>
      <input type="text" id="dishName" name="dishName" required>

      <label for="dishDescription">Введите описание блюда:</label>
      <textarea id="dishDescription" name="dishDescription" required></textarea>

      <label for="dishPrice">Цена:</label>
      <input type="number" id="dishPrice" name="dishPrice" required>

      <div class="buttons-container">
        <input type="submit" value="Добавить в базу данных" class="button">
        <input type="submit" value="Создать бизнес ланч" class="button">

      </div>
    </form>
  </div>


</body>
</html>
'''
        else:
            return "ошибка регистрации"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
