import pyrebase 
import threading
import time

def sendmessage(message,target):
        db.child(target).push({"message": message} , user['idToken'])
def pullfunction():
        while 1:
                time.sleep(1)
                realitycheck = db.child(usrname.replace("@","_").replace(".",",")).get().val()
                #print(type(realitycheck))
                if(not (realitycheck is None) ):
                        pulldata = [x for x in db.child(usrname.replace("@","_").replace(".",",")).get().val().values()]
                        pullkeys = [x for x in db.child(usrname.replace("@","_").replace(".",",")).get().val().keys()]
                        #print(pulldata)
                        #print(pulldata.replace("_","@").replace(",","."))
                        for i in pullkeys:
                                db.child(usrname.replace("@","_").replace(".",",")).child(i).remove()
                        for i in range(len(pulldata)):
                                print([message for message in pulldata[i].values()][0])

config = {  "apiKey": "AIzaSyBcqfP5f1AZ2fDq9ktvNQ9MwXGQeD379a8" ,  "authDomain": "secretmessenger-e9bd3.firebaseapp.com",  "databaseURL": "https://secretmessenger-e9bd3.firebaseio.com",  "storageBucket": "secretmessenger-e9bd3.appspot.com"} 
firebase = pyrebase.initialize_app(config)
auth = firebase.auth() #authenticate a user 
namefile = open("usrinfo.txt","r")
usrname = namefile.readline()
namefile.close()
usrname = usrname.strip('\n')
user = auth.sign_in_with_email_and_password(usrname, "badpassword")
db = firebase.database()
pullthread = threading.Thread(target = pullfunction)
pullthread.start()
while(1):
        print("recipient:")
        target = input().replace("@","_").replace(".",",")
        print("message:")
        message = usrname + ":" + input()
        sendmessage(message,target)



