#coding:utf-8
#Copyright (c) 2015 zhaoming@xiachufang.com All rights reserved.
import decimal
import sys
import os
import requests
import gevent
import time
import simplejson as json
import datetime
import logging
import gevent

s = requests.Session()
urls='https://www.xiachufang.com/js/homepage.6e18aafb.compress.js'
url='http://www.xiachufang.com/js/homepage.6e18aafb.compress.js'


def calc_time(func):
    #@functools.wraps(func)
    def wrapper (*args, **kw):
        t1 = time.time()
        retlist = func(*args, **kw)
        used = int((time.time() - t1) * 1000)
        #used = time.time() - clk
        print('call %s used:%.3f' % (func.__name__, used))
        return retlist
    return wrapper

def get_request(url, payload=None, time_out=10):
    clk = time.time()
    r = requests.request('GET', url, data=payload, timeout=time_out)
    #r = s.request('GET', url, data=payload, timeout=time_out)
    used = int((time.time() - clk) * 1000)
    open('css', 'w').write(r.text.encode('UTF-8'))
    print 'status:', r.status_code, 'used: ', used
    if r.status_code == 503:
        print unicode(r.text)
    return r, True, None


for x in xrange(1000):
    _, ret, _ = get_request(url)
    _, ret, _ = get_request(urls)
