#!/usr/bin/python
import gevent
from gevent_zeromq import zmq
import signal
import os

def server():
    context = zmq.Context()
    server_socket = context.socket(zmq.REP)
    server_socket.bind("tcp://127.0.0.1:5000")

    while True:
        # Implicit context switch occurs here
        msg = server_socket.recv()
        print('Switched to Server for %s ' % msg)
        server_socket.send("hi from server")

def client():
    context = zmq.Context()
    client_socket = context.socket(zmq.REQ)
    client_socket.connect("tcp://127.0.0.1:5000")

    for request in range(1,10):
        client_socket.send("hi from client")
        # Implicit context switch occurs here
        msg = client_socket.recv()
        print('Switched to Client for %d %s' % (request, msg))

def main():
    #gevent.signal(signal.SIGQUIT, os.exit)
    publisher = gevent.spawn(server)
    client    = gevent.spawn(client)
    gevent.joinall([publisher, client])


main()
