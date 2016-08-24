from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"
    
@application.route("/status")
def status():
    return "I'm alive on " + str(socket.gethostbyname(socket.gethostname()))

if __name__ == "__main__":
    application.run()
