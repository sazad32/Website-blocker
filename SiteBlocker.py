#!/usr/bin/env python

"""Makes a simple modification to the user Hosts file."""

__author__ = "Saimoon Azad"
__copyright__ = "Copyright 2018 Saimoon Azad"
__credits__ = ["Saimoon Azad","Ryan Fleck"]

import re

host_address = raw_input("Enter the full path of the host file: ")
ip_address = r"127.0.0.1"
if( not re.match("(.*)\\hosts$", host_address) ):
    host_address = host_address + "\hosts"

choice = raw_input("Would you like to block a website, or remove a site from the blocked list? \nEnter B for blocking, or R for removing ")
blockList = []

if choice.upper() == 'B':
    while(True):
        site_name= raw_input("Enter name of the site or sites you want to block, Press D when done: ")
        if(site_name.upper() == 'D'):
            break
        blockList.append(site_name)
    for l in blockList:
        with open(host_address, 'a') as f:
            f.write("\n" + ip_address + " " + l)
            f.close()

if choice.upper() == 'R':
    f = open(host_address,"r")
    lines = f.readlines()
    f.close()
    while(True):
        site_name= raw_input("Enter name of the site or sites you want to unblock, Press D when done: ")
        if(site_name.upper() == 'D'):
            break
        blockList.append(site_name)
    f = open(host_address,"w")
    for line in lines:
        if not any(l in line for l in blockList):
            f.write(line)
    f.close()

