#!/usr/bin/python
from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
import random
import signal


cond_signal = gevent.event()


print cond_signal


