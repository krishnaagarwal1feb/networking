#!/usr/bin/env python 

import socket			 
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_options("-p", "--port",dest="port_num", help="Reserve a port number for the server to listen")
    (options,arguments) = parser.parse_args()
    if not options.port_num:
        parser.error("[-] Please specify the port number to listen at, use --help for more info. ")
    return options

def create_server(port_num):
    print("[+] Hosting server at port : " + port_num)
    # next create a socket object 
    s = socket.socket()		 
    print("Socket successfully created")

    # reserve a port on your computer in our  
    port = port_num
    """
    Next bind to the port 
    we have not typed any ip in the ip field 
    instead we have inputted an empty string 
    this makes the server listen to requests 
    coming from other computers on the network
    """
    s.bind(('', port))		 
    print "socket binded to %s" %(port) 

    # put the socket into listening mode 
    s.listen(5)	 
    print("socket is listening")

    # a forever loop until we interrupt it or 
    # an error occurs 
    while True: 

        # Establish connection with client. 
        c, addr = s.accept()	 
        print 'Got connection from', addr
        # send a thank you message to the client. 
        c.send('Thank you for connecting') 
        # Close the connection with the client 
        c.close() 

options = get_args()
create_server(options.port_num)
