#!/usr/bin/env python
#Author: Mike R
#Written July 2016
#Manually pull data for desired robots. 
#Type q to exit. Website format must be in http://website.com and then program pulls the robots.txt file.

import urllib2

while(True):
 userRequest=raw_input("Type the base site (such as twitter.com) Type q to quit\n")
 if userRequest == 'q':
    break
 target = open("robots.txt", 'a')

 #check validity of the website
 #if valid, print completion statement
 response = urllib2.urlopen(userRequest + '/robots.txt')
 html = response.read()
 target.write("Robots.txt for " + userRequest)
 target.write("\n")
 target.write(html)
 target.write("\n")
