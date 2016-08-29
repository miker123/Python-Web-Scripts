#!/usr/bin/env python
#Author: Michael R
#Date 8/22/2016
#Description: Download a list of all of the Safari Extensions
# They can later be downloaded, extracted, and analyzed

import urllib2, os, bs4

#getting everything setup
allExts=open('allExts.txt', 'a')


#----------------------------------------------------------
#Get list of all available extensions
#----------------------------------------------------------
url="https://safari-extensions.apple.com/extensions/extensions.json"

get = urllib2.urlopen(url).read()
dom = bs4.BeautifulSoup(get, "html.parser")

downloadURL="https://safari-extensions.apple.com/extensions/"


allExts.write("To download an extension, the url is:\n" + downloadURL + "com.whatever/file name\nReplace com.name with the com.name of the file.\nReplace the file name with the .safariextz file name\n")
#write data to the file
allExts.write(dom.get_text())
