import socket
from flask import Flask, render_template
from flask_restful import Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from flask_opentracing import FlaskTracing
from jaeger_client import Config
from os import getenv

application = Flask(__name__)

config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                'logging': True,
                                'local_agent':
                                {'reporting_host': getenv('JAEGER_HOST', 'localhost')}},
                service_name=getenv('JAEGER_SERVICE_NAME', __name__))
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, application, [])

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
