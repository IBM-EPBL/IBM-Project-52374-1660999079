
from flask import (Flask, render_template)

app =  Flask(__name__)


@app.route('/weather')
def weather():
       return render_template('weatherinfo/weatherpage.html')

#================================= server details ====================================== 

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)