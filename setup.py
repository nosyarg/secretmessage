import pyrebase 
def init():
        config = {  "apiKey": "AIzaSyBcqfP5f1AZ2fDq9ktvNQ9MwXGQeD379a8" ,  "authDomain": "secretmessenger-e9bd3.firebaseapp.com",  "databaseURL": "https://secretmessenger-e9bd3.firebaseio.com",  "storageBucket": "secretmessenger-e9bd3.appspot.com"} 
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth() #authenticate a user 
        user = auth.sign_in_with_email_and_password("graysonyork23@gmail.com", "badpassword")
        db = firebase.database()


def sendmessage():
        message = {"target": "Renzogbenavides@gmail.com", "message": "HELLO"} 
        db.child("messages").push(message, user['idToken'])

init()
sendmessage()
