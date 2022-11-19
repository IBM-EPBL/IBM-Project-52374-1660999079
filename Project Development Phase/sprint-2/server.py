from flask import (Flask, redirect, render_template, render_template_string,
                   request, session, url_for)

@app.route('/home')
def userdata():
       print(email)
       url = (' https://newsapi.org/v2/top-headlines?country=in&apiKey=7c7062c3a98649b5bc6ffda7fdc5a01b')
       TopHeadlinesResponse = requests.get(url).json()
       return render_template('index.html',responseData=TopHeadlinesResponse)

@app.route('/redirectHome')
def redirectHome():
       return redirect('/home')


@app.route('/aboutus')
def aboutus():
       return render_template('aboutus.html')


@app.route('/weather')
def weather():
       return render_template('weatherinfo/weatherpage.html')

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


@app.route('/logout')
def logoutform():
       email = ''
       return render_template('login.html', msg= 'successfully logged out')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)