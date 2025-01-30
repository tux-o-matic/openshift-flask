import os

access_logfile = None
worker_class = os.environ.get('GUNICORN_WORKER_CLASS', 'gevent')

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
