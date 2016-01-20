#!/usr/bin/env python

#Given the Chrome Extension GUIDs, return the name of the extension
#Accepts GUIDs in CSV file

import urllib2, csv, sys

#open CSV File
f = open('file.csv', 'rt')
wf=open('file2.txt', 'w')
try:
    reader = csv.reader(f)
    for row in reader:
	#turning the cvs GUIDs to strings
	test=str(row).strip('[]') 
	newTest= test.replace("'","")
	#setting URL
	URL='https://chrome.google.com/webstore/detail/' + newTest
	#going to site. Get the desired extensions
	response = urllib2.urlopen(URL)
	site=response.geturl()

	#URL returns https://chrome.google.com/webstore/detail/calmly-writer/adhdlhedoenicbbncfckobjedmboleig?hl=en
	#Remove https://chrome.google.com/webstore/detail/
	newSite = site[42:]

	#remove the Extension GUID, everything after the /
	head, sep, tail = newSite.partition('/')
	print head
	wf.write(newTest + head)

finally:
    f.close()
