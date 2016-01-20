#!/usr/bin/env python

#Author: Mike R
#Date: 1/20/2016
#Purpose: Program to return the name of the Chrome Extension if given the GUID

import urllib2

#Program will go to Chrome Web store and name of extension/app of the desired extensions is in URL.
response = urllib2.urlopen('https://chrome.google.com/webstore/detail/adhdlhedoenicbbncfckobjedmboleig')

site=response.geturl()

#URL returns https://chrome.google.com/webstore/detail/calmly-writer/adhdlhedoenicbbncfckobjedmboleig?hl=en

#Remove https://chrome.google.com/webstore/detail/
newSite = site[42:]

#remove the Extension GUID, everything after the /
head, sep, tail = newSite.partition('/')
print head
