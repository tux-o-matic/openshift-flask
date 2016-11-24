import os

access_logfile = os.environ.get('ACCESS_LOGFILE', None)
workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
worker_class = os.environ.get('GUNICORN_WORKER_CLASS', 'sync')
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
