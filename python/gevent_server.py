#!/usr/bin/python
#copyright@xiachufang 2015
from gevent.pywsgi import WSGIServer
import gevent
import os
from third_platform import service

CNT = 0
def task(n):
    print('at %d' % os.getpid())
    #gevent.sleep(2)
    string = ('at %d waked up' % n)
    print(string)
    return str

def application(environ, start_response):
    status = '200 OK'
    headers = [
    ('Content-Type', 'text/html')
    ]
    start_response(status, headers)
    global CNT
    CNT = CNT + 1
    yield "<p>Hello %d " % CNT
    task(CNT)
    yield "World</p>"

gevent.spawn(service.start_pool_server).start()
WSGIServer(('', 8000), application, log=None).serve_forever()
