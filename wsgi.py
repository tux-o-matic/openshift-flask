from flask import Flask, render_template
from flask_restful import Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
import socket

application = Flask(__name__)

api = swagger.docs(Api(application), apiVersion='0.1',
                   basePath='http://localhost:8080',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec', description='API Spec')

@application.route("/")
def index():
    return render_template('index.html', title='Home')
    
@application.route("/status")
def status():
    return "I'm alive on " + str(socket.gethostbyname(socket.gethostname()))
  
@application.route("/metrics")
def metrics():
    return 'flask{host="' + str(socket.gethostbyname(socket.gethostname())) + '",} 0.0'

if __name__ == "__main__":
    application.run()
