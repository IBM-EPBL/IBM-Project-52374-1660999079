from flask import (Flask, redirect, render_template, render_template_string,
                   request, session, url_for)
from markupsafe import escape
import bcrypt
import requests

app =  Flask(__name__)

@app.route('/')
def index():
  return render_template('signup.html')

@app.route('/signUpFormData',methods = ['POST', 'GET'])
def signUpFormData():
         if request.method == "POST":
              userName = request.form.get("userName",False)
              userEmail = request.form.get("userEmail")
              userPassword = request.form.get("userPassword")
              userConfirmPassword = request.form.get("userPasswordConfirm")
              userMobile = request.form.get("userMobile")
              picture = request.form.get("picture")

              if userPassword == userConfirmPassword:
                     sql = "SELECT * FROM news_tracker_application WHERE userEmail =?"
                     stmt = ibm_db.prepare(conn, sql)
                     ibm_db.bind_param(stmt,1,userEmail)
                     ibm_db.execute(stmt)
                     account = ibm_db.fetch_assoc(stmt)
                     # print(account)

                     bytes = userPassword.encode('utf-8')

                     salt = bcrypt.gensalt()

                     hashed_password = bcrypt.hashpw(bytes, salt)
        
                     userPassword = hashed_password


                     if account:
                            return render_template('login.html', msg="You are already a member, please login using your details")
                     else:
                            insert_sql = "INSERT INTO news_tracker_application VALUES (?,?,?,?,?)"
                            
                            # DataBase details will be added in future
   
                            return render_template('login.html', msg="user Data saved successfuly.. Please login use your credentials")
                     
              else:
                     return render_template('signup.html', msg = 'Password and Confirm Password are not matched' )

@app.route('/login')
def login():
       return render_template('login.html')

@app.route('/loginForm', methods=['GET', 'POST'])
def loginForm():
    if request.method == 'POST':

        global email
        email = request.form['userEmail']
        pwd = request.form['userPassword']

        var = email

        sql = "SELECT * FROM news_tracker_application WHERE userEmail =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        auth_token = ibm_db.fetch_assoc(stmt)
        print("auth",auth_token)

        if auth_token:
            # encoding user password 
            userBytes = pwd.encode('utf-8')
            byte_pwd = bytes(auth_token['password saved in DataBase'], 'utf-8')

            # checking password
            result = bcrypt.checkpw(userBytes, byte_pwd)
            
            if result:
                print("succ")
                url = (' https://newsapi.org/v2/top-headlines?country=in&apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
                TopHeadlinesResponse = requests.get(url).json()
                return render_template('index.html', msg="Logged in Successfully", responseData=TopHeadlinesResponse, tmp = 1)
            else:
                return render_template('login.html', msg="Invalid Credentials", tmp = 0)
        else:
            return render_template('signup.html', msg="User doesn't exist, Please Register using your details!")
    else:  
        return render_template('login.html', title='Sign In')

@app.route('/aboutus')
def aboutus():
       return render_template('aboutus.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)