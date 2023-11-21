from datetime import datetime
from app import app, db
from app.models import Users, Messages
from flask import request, redirect
import sqlalchemy

@app.route('/', methods=['GET'])
def index():
    return """
    Welcome to the home page!

    Available Routes:

    1. User Registration
       - Endpoint: /register
       - Method: POST
       - Description: Register a new user with the provided username and password.
       - Parameters:
         - username: User's username.
         - password: User's password.
         - confirmPassword: Confirm the password.
       - Example usage:
         curl -X POST "http://127.0.0.1:8080/register?username=user&password=pass&confirmPassword=pass"

    2. Add Message
       - Endpoint: /send
       - Method: POST
       - Description: Add a new message from an existing user.
       - Parameters:
         - username: User's username.
         - password: User's password.
         - message: The message to be added.
       - Example usage:
         curl -X POST "http://127.0.0.1:8080/send?username=user&password=pass&message=Hello, world!"

    3. Get All Messages
       - Endpoint: /all
       - Method: GET
       - Description: Retrieve all messages from the database.
       - Example usage:
         curl http://127.0.0.1:8080/all
    """

@app.route('/register', methods=['POST'])
def addUser():
    try:
        if request.args == None:
            raise ValueError("Empty args!\n")
        username = request.args.get("username")
        password = request.args.get("password")
        confirmPassword = request.args.get("confirmPassword")
        if (password != confirmPassword):
            raise ValueError("Passwords dont match!\n")
        
        sql = sqlalchemy.text("SELECT * FROM users WHERE username=:username")
        user = db.session.execute(sql, {"username": username}).fetchone()
        print(user)
        if user:
            raise ValueError("User already exists!\n")
        
        db.session.add(Users(username = username, password = password))
        db.session.commit()
        return "User registration successful.\n" + getMessagesFromInText()
    except Exception as e:
        return "ERROR: {}".format(str(e))


@app.route('/send', methods=['POST'])
def addMessage():
    try:
        if request.args == None:
            raise ValueError("Empty args!\n")
        username = request.args.get("username")
        password = request.args.get("password")
        message = request.args.get("message")

        sql = sqlalchemy.text("SELECT * FROM users WHERE username=:username")
        user = db.session.execute(sql, {"username": username}).fetchone()

        if not user or user.password != password:
            raise ValueError("Password doesent match!\n")
        
        db.session.add(Messages(userId = user.id, message = message, messageDate = datetime.utcnow()))
        db.session.commit()
        return "Message added successfully.\n" + getMessagesFromInText()
    except Exception as e:
        return "ERROR: {}".format(str(e))

@app.route('/all', methods=['GET'])
def getMessages():
    try:
        return getMessagesFromInText()
    except Exception as e:
        return "ERROR: {}".format(str(e))
    
def getMessagesFromInText():
    answer = []
    try:
        sql = sqlalchemy.text("SELECT * FROM Messages")
        for message in db.session.execute(sql):
            answer.append(f"Message from user {message.userId} on {message.messageDate} : {message.message}")
        return "\n".join(answer) + "\n"
    except Exception as e:
        return "ERROR: {}".format(str(e))