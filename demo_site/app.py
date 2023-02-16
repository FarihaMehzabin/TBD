import traceback
from flask import Flask, render_template, redirect, url_for, request, make_response
import requests
from cookies import cookies

config = {
    "DEBUG": True,  # some Flask specific configs
}


app = Flask(__name__)

cookie = cookies()

@app.route('/')
def index():
    
    cookie_check = cookie.check_for_cookie()
         
    if cookie_check:
        return "Welcome"
    
    return "you're not logged in"

@app.route("/users/login", methods=["POST"])
def login():
    
     error = None
    
     if request.method == 'POST':
         
        cookie_check = cookie.check_for_cookie()
         
        if cookie_check:
            cookie_check.headers['location'] = url_for('index')
            
            return cookie_check, 302 

        response = requests.get(f"http://127.0.0.1:8080/user-login/{request.form['u']}/{request.form['p']}")
        
        res = response.json()
        
        if res['error'] == False:
            
            set_cookie = cookie.set_cookie()
            
            set_cookie.headers['location'] = url_for('index')
            
            return set_cookie, 302
            
        else:
            error = res['message']
            
     
     return render_template('login.html', error = error)


@app.route("/users/signup", methods=["POST"])
def sign_up():
    
     error = None
    
     if request.method == 'POST':
         
        cookie_check = cookie.check_for_cookie()
         
        if cookie_check:
            cookie_check.headers['location'] = url_for('index')
            
            return cookie_check, 302 #How to redirect to some other endpoint with username?
     
        response = requests.get(f"http://127.0.0.1:8080/user-signup/{request.form['firstname']}/{request.form['lastname']}/{request.form['u']}/{request.form['p']}")
        
        res = response.json()
        
        if res['error'] == False:
            set_cookie = cookie.set_cookie()
            
            set_cookie.headers['location'] = url_for('index')
            
            return set_cookie, 302
        else:
            error = res['message']
     
     return render_template('signup.html', error = error)
    

# Cookie checker
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('session')
   
   print(name)
   
   return '<h1>welcome ' + name + '</h1>'   

app.run(host='0.0.0.0', port=2520)


# todo

# For every signed up user, there should be a GUID to keep track?