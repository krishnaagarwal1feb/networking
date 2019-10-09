#!/usr/bin/env python 

# Import socket module 
import socket			 
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_options("-ip", "--InternetProtocol", dest="ip_address", help="Server's IP address to which the client needs to connect.")
    parser.add_options("-p", "--port",dest="port_num", help="port number at which the server is listening")
    (options,arguments) = parser.parse_args()
    if not options.ip_address:
        parser.error("[-] Please specify the IP address of server to establish connection, use --help for more info. ")
    elif not options.port_num:
        parser.error("[-] Please specify the port number at which the server is listening, use --help for more info. ")
    return options

def connect_to_server(ip_address, port_num):
    print("[+] Connecting to server at IP : " + ip_address + " at port : " + port_num)
    
    # Create a socket object 
    s = socket.socket()		 

    # Define the port on which you want to connect 
    port = port_num				

    # connect to the server on local computer 
    s.connect((ip_address, port)) 

    #receive data from the server 
    print s.recv(1024) 
    
    # close the connection 
    s.close()	 

options = get_args()
connect_to_server(options.ip_address, options.port_num)

