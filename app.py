from flask import Flask
from pymongo import MongoClient
from datetime import datetime
from flask import request

app = Flask(__name__)
messages = MongoClient("mongodb://db1.local:27017,db2.local:27017,db3.local:27017/?replicaSet=rs0")["chat"]["messages"]

print(messages)

@app.route('/')
def hello():
    message = request.args.get('message')
    if message:
        messages.insert({"timestamp": str(datetime.now()), "message": message})

    n = messages.count()
    ret = ""  
    if n > 10:
        n = n - 10
        all_msgs = messages.find().skip(n)
    else:
        all_msgs = messages.find()

    for mes in all_msgs:
        ret += "<p>"+str(mes["timestamp"]) + "<br>" + mes["message"] + "</p>"
    
    return ret

if __name__ == '__main__':
    app.run(host='0.0.0.0')
