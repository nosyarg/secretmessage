import pyrebase 

def sendmessage(message,target):
        db.child("messages").push({"target": target, "message": message} , user['idToken'])
def getmessage():
        print("FUCK")

config = {  "apiKey": "AIzaSyBcqfP5f1AZ2fDq9ktvNQ9MwXGQeD379a8" ,  "authDomain": "secretmessenger-e9bd3.firebaseapp.com",  "databaseURL": "https://secretmessenger-e9bd3.firebaseio.com",  "storageBucket": "secretmessenger-e9bd3.appspot.com"} 
firebase = pyrebase.initialize_app(config)
auth = firebase.auth() #authenticate a user 
user = auth.sign_in_with_email_and_password("graysonyork23@gmail.com", "badpassword")
db = firebase.database()
while(1):
        print("recipient:")
        target = input()
        print("message:")
        message = input()
        sendmessage(message,target)
