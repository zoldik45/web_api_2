import sqlite3

from flask import Flask, url_for
from flask import request, redirect
from flask import render_template
import webbrowser


app = Flask(__name__)

def get_dishes():
    conn = sqlite3.connect('bluda.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, cena FROM eda")
    dishes = cursor.fetchall()
    conn.close()
    return dishes




def calculate_lunch_price(dishes):
    conn = sqlite3.connect('bluda.db')
    cursor = conn.cursor()
    prices = []
    for dish in dishes:
        cursor.execute("SELECT cena FROM eda WHERE name = ?", (dish,))
        price = cursor.fetchone()[0]
        prices.append(price)
    conn.close()
    return sum(prices)


def add_lunch_to_database(first_dish, second_dish, dessert, drink, lunch_price):
    conn = sqlite3.connect('lanchi.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lanchi (pervoe, vtoroe, desert, napitochek, cenna) VALUES (?, ?, ?, ?, ?)", (first_dish, second_dish, dessert, drink, lunch_price))
    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        dishes = get_dishes()
        return render_template('registration.html', dishes=dishes)
    elif request.method == 'POST':
        first_dish = request.form['first_dish']
        second_dish = request.form['second_dish']
        dessert = request.form['dessert']
        drink = request.form['drink']
        with sqlite3.connect('lanchi.db') as db:
            cursor = db.cursor()
            query_1 = """INSERT INTO lanchi (pervoe, vtoroe, desert, napitochek, cenna) VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(query_1, (first_dish, second_dish, dessert, drink))  # Использование параметров запроса
            db.commit()
        return 'всё круто'

@app.route('/create_lunch', methods=['POST'])
def create_lunch():
    first_dish = request.form['first_dish']
    second_dish = request.form['second_dish']
    dessert = request.form['dessert']
    drink = request.form['drink']
    dishes = [first_dish, second_dish, dessert]
    lunch_price = calculate_lunch_price(dishes)
    add_lunch_to_database(first_dish, second_dish, dessert, drink, lunch_price)
    return webbrowser.open_new_tab('http://127.0.0.1:8080/')






@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        dishes1 = get_dishes()
        return render_template('novi.html', dishes=dishes1)
    elif request.method == 'POST':
        c = request.form['dishName']
        d = request.form['dishDescription']
        e = request.form['dishPrice']
        dish_to_delete = request.form['deleteDish']
        print("1")
        if request.form['submit'] == 'Добавить в базу данных':
            print('2')
            with sqlite3.connect('bluda.db') as db:
                cursor = db.cursor()
                query_1 = """INSERT INTO eda (name, opisanie, cena) VALUES (?, ?, ?)"""
                cursor.execute(query_1, (c, d, e))
                db.commit()
                return 'Данные успешно добавлены в базу данных'
        elif request.form['submit'] == 'Удалить из базы данных':
            print('3')
            with sqlite3.connect('bluda.db') as db:
                cursor = db.cursor()
                query_2 = """DELETE FROM eda where name = ?"""
                cursor.execute(query_2, (dish_to_delete,))
                db.commit()
                return 'ewdddscsddcdscsd'
        return 'ewdddscsddcdscsd'

       # elif request.form['submit'] == 'Создать бизнес ланч':
           # return webbrowser.open_new_tab('')

@app.route('/delete_dish', methods=['POST', 'GET'])
def deleteThisDish():
    if request.method == 'POST':
        dish_to_delete = request.form['deleteDish']
        print('ёп', dish_to_delete)
        print(request.form)
        with sqlite3.connect('bluda.db') as db:
            cursor = db.cursor()
            query_2 = """DELETE FROM eda where name = ?"""
            cursor.execute(query_2, (dish_to_delete,))
            db.commit()
            return 'ewdddscsddcdscsd'


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
            return webbrowser.open_new_tab('http://127.0.0.1:8080/form_sample')
        else:
            return "ошибка регистрации"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
