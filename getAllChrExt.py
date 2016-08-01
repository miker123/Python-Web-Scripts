#!/usr/bin/env python
#Written By Mike R
#August 1st, 2016

#This program does the following:
#Finds all Chrome Extensions
#Writes the URLs from sitemap to a file
#Write all of the extension IDs to a separate .txt file

import urllib2, urllib
#get raw site data
global sites
sites=[]

#get refined data for sites
global extSites
extSites=[]
f=open("extensionURLS.txt", "w")
f2=open("extensionURLS.txt", "r")
f3=open("extendData.txt", "w")
def homepage():
    
    file = urllib2.urlopen('https://chrome.google.com/webstore/sitemap?shard=0&numshards=0')
    data = file.readlines()
    file.close()
    #read lines above, now separate what we want below.
    for l in data:
        if "<loc" in l:
            sites.append(l)
#get the data for extensions
homepage()


for l in sites:
    l=l.replace("<loc>","")
    l=l.replace("</loc>","")
    new_str = l.replace('amp;', '')
    f.write(new_str)
    extSites.append(new_str)

f.close()
for line in f2:
    #print "Site is: " + line
    try:
        file2 = urllib2.urlopen(line)
        data2 = file2.readlines()
        file2.close()
        for M in data2:
            if "<loc" in M:
                M=M.replace("<loc>","")
                M=M.replace("</loc>","")
                #remove URL so can just get full extension
                M=M.replace("https://chrome.google.com/webstore/detail/", "")
                M=M.split("/")[1]
                f3.write(M)
                #download all files to whatever location software is running from


    except:
        print ""
