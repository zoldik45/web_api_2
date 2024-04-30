from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE_BLUDA = 'bluda.db'
DATABASE_LANCHI = 'lanchi.db'

def query_db(query, args=(), one=False, db_path=DATABASE_BLUDA, write=False):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query, args)
    if write:
        conn.commit()
        result = True
    else:
        rv = cursor.fetchall()
        result = (rv[0] if rv else None) if one else rv
    cursor.close()
    conn.close()
    return result

@app.route('/')
def index():
    dishes = query_db("SELECT name, cena FROM eda")
    lunches = query_db("SELECT id, pervoe, vtoroe, desert, napitochek, cenna FROM lanchi", db_path=DATABASE_LANCHI)
    return render_template('lanchi.html', dishes=dishes, lunches=lunches)

@app.route('/create_lunch', methods=['POST'])
def create_lunch():
    first_dish = request.form['first_dish']
    second_dish = request.form['second_dish']
    dessert = request.form['dessert']
    drink = request.form['drink']
    dishes_selected = [first_dish, second_dish, dessert, drink]
    total_price = sum([query_db("SELECT cena FROM eda WHERE name = ?", [dish], one=True)[0] for dish in dishes_selected])
    query_db("INSERT INTO lanchi (pervoe, vtoroe, desert, napitochek, cenna) VALUES (?, ?, ?, ?, ?)",
             (first_dish, second_dish, dessert, drink, total_price), db_path=DATABASE_LANCHI, write=True)
    return redirect(url_for('lanchi.html'))

@app.route('/delete_lunch', methods=['POST'])
def delete_lunch():
    lunch_id = request.form['lunch_id']
    query_db("DELETE FROM lanchi WHERE id = ?", [lunch_id], db_path=DATABASE_LANCHI, write=True)
    return redirect(url_for('lanchi.html'))

if __name__ == '__main__':
    app.run(debug=True)
