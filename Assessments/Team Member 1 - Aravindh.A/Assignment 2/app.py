from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def basicpage():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signin')
def signin():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
