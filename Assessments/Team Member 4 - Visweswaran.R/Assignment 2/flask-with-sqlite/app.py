from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session, render_template_string
from markupsafe import escape
import sqlite3 as sql
import ibm_db

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/signin')
def signin():
  return render_template('signin.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/logout')
def logout():
  return render_template('logout.html')

@app.route('/aboutus')
def aboutus():
  return render_template('aboutus.html')

def get_db():
    conn = sql.connect('signup_database.db')
    conn.row_factory = sql.Row
    return conn

@app.route('/signup',methods = ['POST', 'GET'])
def signup_page():
  if request.method == 'POST':
    try:
      name = request.form['name']
      username = request.form['username']
      address = request.form['address']
      password = request.form['password']
         
      with sql.connect("signup_database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (name,username,address,password) VALUES (?,?,?,?)",(name,username,address,password) )
        con.commit()
        msg = "Record successfully added!"
    except:
      con.rollback()
      msg = "error in insert operation"

    finally:
      return render_template("home.html",msg = "created")
      con.close()

@app.route('/signin', methods=('GET', 'POST'))
def signin_page():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT password FROM users WHERE username = ?', (username, )
        ).fetchone()
        
        if user is None:
            error = 'Incorrect Username/Password.'
        elif password != user['password']:
            print(user)
            error = 'Incorrect Password.'

        if error is None:
            return render_template("logout.html")
        db.close()

    return render_template('signin.html', title='Sign In', error=error)

@app.route('/logout', methods=('GET', 'POST'))
def logout_page(nme, adrss):
    error = None
    if request.method == 'POST':
        username = request.form['username']
        db = get_db()
        nme = db.execute(
          'SELECT name FROM users WHERE username = ?', (username, )
          ).fetchone()
        adrss = db.execute(
           'SELECT address FROM users WHERE username = ?', (username, )
          ).fetchone()
        return render_template(
          'logout.html',
          msg1=nme,
          msg2=adrss)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
