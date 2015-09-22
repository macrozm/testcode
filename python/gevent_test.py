#!/usr/bin/python
from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
import random
import signal

url1='http://www.baidu.com'
url2='http://www.sina.com'
url3='http://www.xiachufang.com'

ev = []

def f(url, n):
    print('GET: %s %d' % (url, n))
    #resp = urllib2.urlopen(url)
    #data = resp.read()
    #print('%d %d bytes received from %s.' % (n, len(data), url))
def oldfun():
    ev.append(gevent.spawn(f, url1, 1))
    ev.append(gevent.spawn(f, url2, 2))
    ev.append(gevent.spawn(f, url3, 3))
    for e in ev:
        e.start()
        e.join()
    gevent.joinall(ev)

def task(pid):
    gevent.sleep(random.randint(0,2) * 0.001)
    print("task:%d" % pid)
    gevent.sleep(1)

def proc_req(x, y):
    for n in range(x, y):
        ev.append(gevent.spawn(task, n))
    print("fire then up")
    for e in ev:
        e.start()
        #print("join it")
        #e.join()
    print("do sometin else in proc")
    gevent.sleep(1)
    print("wake up")
    return 'aa', 'bb', 'cc'

def shutdown():
    print 'catch signals'
    os.exit()

def main():
    gevent.signal(signal.SIGQUIT, shutdown)
    s = gevent.signal(signal.SIGINT, shutdown)
    print s
    g = gevent.spawn(proc_req, 1, 6)
    print 'start\n', g
    g.start()
    g.join()
    print g.value, 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'
    x, y, = g.value[0:2]
    print x, y
    #gevent.spawn(proc_req, 7, 11).join()


main()
