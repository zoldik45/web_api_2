from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Получим список блюд из базы данных
    conn = sqlite3.connect('bluda.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM eda")
    dishes = cursor.fetchall()
    conn.close()

    return render_template('index.html', dishes=dishes)

@app.route('/create_lunch', methods=['POST'])
def create_lunch():
    first_dish = request.form.get('first_dish')
    second_dish = request.form.get('second_dish')
    dessert = request.form.get('dessert')
    drink = request.form.get('drink')

    # Выполните необходимые расчеты, чтобы определить стоимость ланча
    conn = sqlite3.connect('bluda.db')
    cursor = conn.cursor()
    cursor.execute("SELECT cena FROM eda WHERE name IN (?, ?, ?)", (first_dish, second_dish, dessert))
    prices = cursor.fetchall()
    conn.close()
    lunch_price = sum([price[0] for price in prices])

    # Занесите данные ланча в базу данных
    conn = sqlite3.connect('lanchi.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lanchi (pervoe, vtoroe, desert, napitochek, cenna) VALUES (?, ?, ?, ?, ?)", (first_dish, second_dish, dessert, drink, lunch_price))
    conn.commit()
    conn.close()

    # Перенаправим пользователя на главную страницу с сообщением об успешном создании ланча
    return redirect(url_for('index', lunch_created=True, lunch_price=lunch_price))

if __name__ == '__main__':
    app.run()
