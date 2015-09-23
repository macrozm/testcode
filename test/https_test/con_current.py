#coding:utf-8
#Copyright (c) 2015 zhaoming@xiachufang.com All rights reserved.
import gevent
from gevent import monkey
gevent.monkey.patch_all()
from gevent.pool import Group
import decimal
import sys
import os
import requests
import gevent
import time
import simplejson as json
import datetime
import logging
import signal

hs = requests.Session()
s = requests.Session()

result = {
            'http': [],
            'https': [],
            'http_sess':[],
            'https_sess':[],
    }

group = Group()

def get_request(url, payload=None, time_out=10, sess=None):
    clk = time.time()
    try:
        if not sess:
            r = requests.request('GET', url, data=payload, timeout=time_out)
        else:
            r = sess.request('GET', url, data=payload, timeout=time_out)
    except:
        return 400, 0, 0, 0

    used = int((time.time() - clk) * 1000)

    if r.status_code != 200: return 400, 0, 0, 0

    if r.raw.seekable():
        r.raw.seek(2)
        length = r.raw.tell()
    else:
        length = int(r.headers.get('content-length', 0)) or len(r.content)
    return r.status_code, length, used, length*1000/used

def func(lst, url, sess):
    st, l, t, weight = get_request(url, sess=sess)
    print url, st, t, sess
    if st != 200:
        return
    lst.append((l, t, weight))

def show_result():
    #print result
    for (k, v) in result.items():
        v = sorted(v, key = lambda e: e[2], reverse=True)
        if len(v) > 500:
            v = v[:-100]
        byte, time = reduce(lambda x,y :  (x[0]+y[0], x[1]+y[1]), v)
        print "%s avg_time:%d avg_size:%d" % (k, time/len(v), byte/len(v))

def signal_proc(a, b):
    show_result()
    os._exit(0)

def main():
    signal.signal(signal.SIGINT, signal_proc)
    midurl = '://www.xiachufang.com/'
    for n, line in enumerate(open('res')):
        line = line.strip()
        g1 = gevent.spawn(func, result['https'],        'https' + midurl + line, None)
        g2 = gevent.spawn(func, result['https_sess'],   'https' + midurl + line, hs)
        g3 = gevent.spawn(func, result['http'],         'http' + midurl + line, None)
        g4 = gevent.spawn(func, result['http_sess'],    'http' + midurl + line, s)
        group.add(g1)
        group.add(g2)
        group.add(g3)
        group.add(g4)
        group.join()
        print n
        #if n > 10: break
    show_result()

main()
