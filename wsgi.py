from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"
    
@application.route("/status")
def hello():
    return "I'm alive"

if __name__ == "__main__":
    application.run()
