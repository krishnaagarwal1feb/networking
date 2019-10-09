#!/usr/bin/env python 
# GIVE THE port num in command line , we are using localhost ip here
# Import socket module 
import socket	
import sys

def connect_to_server(port_num):
    ip_address = '127.0.0.1'
    print("[+] Connecting to server at IP : " + ip_address + " at port : " , port_num)
    
    # Create a socket object 
    s = socket.socket()		 

    # Define the port on which you want to connect 
    port = port_num				
    # connect to the server on local computer 
    s.connect((ip_address, port)) 

    #receive data from the server 
    print(s.recv(1024))
    
    # close the connection 
    s.close()	 

connect_to_server( int(sys.argv[1]) )

