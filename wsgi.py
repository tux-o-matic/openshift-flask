from flask import Flask
from flask.ext.restful import Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
import socket

application = Flask(__name__)

api = swagger.docs(Api(application), apiVersion='0.1',
                   basePath='http://localhost:8080',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec', description='API Spec')

@application.route("/")
def hello():
    return "Hello World!"
    
@application.route("/status")
def status():
    return "I'm alive on " + str(socket.gethostbyname(socket.gethostname()))

if __name__ == "__main__":
    application.run()
