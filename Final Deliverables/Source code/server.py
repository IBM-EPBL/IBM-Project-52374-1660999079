import json
import bcrypt
import ibm_db
import requests
from flask import (Flask, redirect, render_template, request)

app =  Flask(__name__)

# ============================================  for database with IBM===========================
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=credientials/DigiCertGlobalRootCA.crt;UID=bgh36879;PWD=TvSzQQQ6Jhaaiwg6",'','')
print(conn)
print("🟢 connection successfull with IBM_DB ⚡")

# signup form data
@app.route('/')
def index():
  return render_template('signup.html')

# signup form validation
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
                            prep_stmt = ibm_db.prepare(conn, insert_sql)
                            ibm_db.bind_param(prep_stmt, 1, userName)
                            ibm_db.bind_param(prep_stmt, 2, userEmail)
                            ibm_db.bind_param(prep_stmt, 3, userPassword)
                            ibm_db.bind_param(prep_stmt, 4, userMobile)
                            ibm_db.bind_param(prep_stmt, 5, picture)
                            ibm_db.execute(prep_stmt)
                  
                  
                            from sendgrid import SendGridAPIClient
                            from sendgrid.helpers.mail import Mail
                  
                            message = Mail(
                                   from_email='applicationnewstracker@gmail.com',
                                   to_emails=userEmail,
                                   subject='Welcome to News Tracker Application',
                                   html_content='<img src="https://cloud-object-storage-18-cos-standard-yx0.s3.jp-tok.cloud-object-storage.appdomain.cloud/welcom_nta.gif" />')
                            try:
                                   sg = SendGridAPIClient('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')
                                   response = sg.send(message)
                                   print(response.status_code)
                                   print(response.body)
                                   print(response.headers)
                            except Exception as e:
                                   print(str(e))
   
                            return render_template('login.html', msg="user Data saved successfuly.. Please login use your credentials")
                     
              else:
                     return render_template('signup.html', msg = 'Password and Confirm Password are not matched' )
                            
# ============================================= for serve  ======================================

# login form validation
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
            byte_pwd = bytes(auth_token['USERPASSWORD'], 'utf-8')

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

# home page
@app.route('/home')
def userdata():
       print(email)
       url = (' https://newsapi.org/v2/top-headlines?country=in&apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
       TopHeadlinesResponse = requests.get(url).json()
       return render_template('index.html',responseData=TopHeadlinesResponse)

# signup form
@app.route('/')
@app.route('/signup')
def signUp():
       return render_template('signup.html')

# login form
@app.route('/login')
def login():
       return render_template('login.html')

# logout
@app.route('/logout')
def logout():
       return redirect('/login')

# redirect Home
@app.route('/redirectHome')
def redirectHome():
       return redirect('/home')

# about us
@app.route('/aboutus')
def aboutus():
       return render_template('aboutus.html')

# weather
@app.route('/weather')
def weather():
       return render_template('weatherinfo/weatherpage.html')

# education
@app.route('/education')
def education():
       value = 'education'
       crimenews = ('https://newsapi.org/v2/everything?' 'q='+value+'&''from=2022-10-29&''sortBy=popularity&''apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
       educationResponse = requests.get(crimenews).json()
       print(educationResponse)
       # return render_template('NewsTemplate.html',responseData=crimeNewsresponse)   dharun API key = 7c7062c3a98649b5bc6ffda7fdc5a01b aravindh = 9b6f57afe98440b8b362b1046559d71d
       result_count = educationResponse.get('totalResults')
       if(result_count>0):
          return render_template('NewsTemplate.html',responseData=educationResponse,returned_input_search_value=value,result_count=result_count)
       else:
          return render_template('notfound.html')

# Top headlines
@app.route('/TopHeadlines')
def TopHeadlines():
       value ='Top Headlines'
       url = (' https://newsapi.org/v2/top-headlines?country=in&apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
       TopHeadlinesResponse = requests.get(url).json()
       result_count = TopHeadlinesResponse.get('totalResults')
       return render_template('NewsTemplate.html',responseData=TopHeadlinesResponse,returned_input_search_value=value,result_count=result_count) 

# science news
@app.route('/sciencenews')
def crimenews():
       value ='science'
       sciencenews = ('https://newsapi.org/v2/everything?' 
       'q='+value+'&'
       'from=2022-10-29&'
       'sortBy=popularity&'
       'apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
       scienceNewsresponse = requests.get(sciencenews).json()
       print(scienceNewsresponse)
       #    dharun API key = 7c7062c3a98649b5bc6ffda7fdc5a01b aravindh = 9b6f57afe98440b8b362b1046559d71d
       result_count =scienceNewsresponse.get('articles')
       result_count = len(result_count)

       if(result_count>0):
          return render_template('NewsTemplate.html',responseData=scienceNewsresponse,returned_input_search_value=value,result_count=result_count)
       else:
          return render_template('notfound.html')

# health news 
@app.route('/healthnews')
def healthnews():
       value = 'health'
       healthnews = ('https://newsapi.org/v2/everything?' 
        'q='+value+'&'
       'from=2022-10-29&'
       'sortBy=popularity&'
       'apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
       healthNewsresponse = requests.get(healthnews).json()
       result_count = healthNewsresponse.get('totalResults')
       if(result_count>0):
          return render_template('NewsTemplate.html',responseData=healthNewsresponse,returned_input_search_value=value,result_count=result_count)
       else:
          return render_template('notfound.html')

# sports news 
@app.route('/sportsnews')
def sportsnews():
       value = 'sports'
       sportsnews = ('https://newsapi.org/v2/everything?' 
       'q='+value+'&'
       'from=2022-10-29&'
       'sortBy=popularity&'
       'apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
       sportsNewsresponse = requests.get(sportsnews).json()
       # return render_template('NewsTemplate.html',responseData=crimeNewsresponse)
       result_count = sportsNewsresponse.get('totalResults')
       if(result_count>0):
          return render_template('NewsTemplate.html',responseData=sportsNewsresponse,returned_input_search_value=value,result_count=result_count)
       else:
          return render_template('notfound.html')

@app.route('/searchResults', methods =["POST"])
def searchResults():
       if request.method == "POST":
              search_value_name = request.form.get("searchvalue")

              print(search_value_name)

              searchURL = ('https://newsapi.org/v2/everything?'
              'q='+search_value_name+'&'
              'from=2022-10-29&'
              'sortBy=popularity&'
              'apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
              
              searchResponse = requests.get(searchURL).json()
              result_count = searchResponse.get('totalResults')

              print(result_count)  # NUMBER

              if(result_count>0):
                 return render_template('NewsTemplate.html',responseData=searchResponse,returned_input_search_value=search_value_name,result_count=result_count)
              else:
                 return render_template('notfound.html',responseData=searchResponse,returned_input_search_value=search_value_name)

# tab user
@app.route('/tabuser')
def tabuser():

       userEmail = email
       print('email',userEmail)
       sql = "SELECT * FROM news_tracker_application WHERE userEmail =?"
       stmt = ibm_db.prepare(conn, sql)
       ibm_db.bind_param(stmt, 1, userEmail)
       ibm_db.execute(stmt)
       auth_token = ibm_db.fetch_assoc(stmt)

       return render_template('userinfo.html', msg=auth_token)

# logout
@app.route('/logout')
def logoutform():
       email = ''
       return render_template('login.html', msg= 'successfully logged out')

#================================= server details ====================================== 

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
