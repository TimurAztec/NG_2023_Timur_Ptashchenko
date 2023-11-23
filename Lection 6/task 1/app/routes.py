from datetime import datetime, timedelta
from app import app, db
from app.models import Users, Messages, Sessions
from flask import request, redirect, make_response, render_template
import hashlib
import sqlalchemy

@app.route('/', methods=['GET'])
def renderChat():
    try:
        sql = sqlalchemy.text("SELECT * FROM Messages")
        messages = db.session.execute(sql)
        return render_template("chat.html", messages = messages)
    except Exception as e:
        return "ERROR: {}".format(str(e))

@app.route('/signup', methods=['GET'])
def renderSignUp():
    try:
        return render_template("signup.html")
    except Exception as e:
        return "ERROR: {}".format(str(e))
    
@app.route('/signin', methods=['GET'])
def renderSignIn():
    try:
        return render_template("signin.html")
    except Exception as e:
        return "ERROR: {}".format(str(e))

@app.route('/signup', methods=['POST'])
def signupUser():
    try:
        if request.form == None:
            raise ValueError("Empty args!\n")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        if (password != confirmPassword):
            raise ValueError("Passwords dont match!\n")
        
        sql = sqlalchemy.text("SELECT * FROM users WHERE username=:username")
        user = db.session.execute(sql, {"username": username}).fetchone()

        if user:
            raise ValueError("User already exists!\n")
        
        db.session.add(Users(username = username, password = hashlib.sha256(password.encode("utf-8")).hexdigest()))
        db.session.commit()

        res = make_response(redirect("/"))
        res.set_cookie("session_id", str(signin(username=username, passwordPlain=password)))
        return res
    except Exception as e:
        return "ERROR: {}".format(str(e))
    
@app.route('/signin', methods=['POST'])
def signinUser():
    try:
        if request.form == None:
            raise ValueError("Empty args!\n")
        username = request.form.get("username")
        password = request.form.get("password")

        res = make_response(redirect("/"))
        res.set_cookie("session_id", str(signin(username=username, passwordPlain=password)))
        return res
    except Exception as e:
        return "ERROR: {}".format(str(e))

def signin(username, passwordPlain):
    sql = sqlalchemy.text("SELECT * FROM users WHERE username=:username")
    user = db.session.execute(sql, {"username": username}).fetchone()

    if hashlib.sha256(passwordPlain.encode("utf-8")).hexdigest() != user.password:
        raise ValueError("Wrong password!\n")

    db.session.add(Sessions(userId = user.id, expires = (datetime.utcnow() + timedelta(hours=24))))
    db.session.commit()

    sql = sqlalchemy.text("SELECT * FROM sessions WHERE userId=:userId")
    session = db.session.execute(sql, {"userId": user.id}).fetchone()
 
    return session.id

@app.before_request
def before_request():
    if request.endpoint in ['renderSignUp', 'renderSignIn', 'signupUser', 'signinUser']:
        return
    
    sessionId = request.cookies.get('session_id')

    sql = sqlalchemy.text("SELECT * FROM sessions JOIN users ON sessions.userId = users.id WHERE sessions.id=:sessionId")
    session = db.session.execute(sql, {"sessionId": sessionId}).fetchone()
    
    if session == None or datetime.fromisoformat(session.expires) < datetime.utcnow():
        return redirect('/signin')
    
    request.session = session

@app.route('/send', methods=['POST'])
def addMessage():
    try:
        if request.form == None:
            raise ValueError("Empty args!\n")
        userId = request.session.userId
        username = request.session.username
        message = request.form.get("message")
        
        db.session.add(Messages(userId = userId, username = username, message = message, messageDate = datetime.utcnow()))
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return "ERROR: {}".format(str(e))
    