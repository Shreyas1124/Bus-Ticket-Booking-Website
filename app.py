#for importing packages required fopr flask app
from flask import Flask,render_template,request,make_response
# for connecting to db
import mysql.connector
from mysql.connector import Error

import json

#initialize the flask app
app=Flask(__name__)

#specifications of routes
@app.route('/index')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bookticket')
def bookticket():
    return render_template('bookticket.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/comment')
def comment():
    return render_template('comment.html')

@app.route('/regdata')
def regdata():
    connection=mysql.connector.connect(host='localhost',database='testdb',user='root',password='')
    named=request.args['apinamed']
    phone=request.args['apiphone']
    email=request.args['apiemail']
    adhaar=request.args['apiadhaar']
    cursor=connection.cursor()
    query="insert into userdata values ('"+named+"','"+phone+"','"+email+"','"+adhaar+"')"
    print(query)
    cursor.execute(query)
    connection.commit()
    cursor.close()
    msg="Data success"
    resp=make_response(json.dumps(msg))
    return resp


    

    
    
    


  


if __name__=='__main__':
    app.run(debug=true)
    #app.run(host="0.0.0.0") to host on other cmptrs
    
