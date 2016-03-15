#!/usr/bin/env python
#Author: Mike R
#Date:3/1/2016
#Opens new browser tab to whatever site the user specifies.

import webbrowser
new = 2 #this specifies the browser to open in a new tab, if possible

#specify the URL
url = "https://www.youtube.com/watch?v=AUChk0lxF44"

#open the URL
webbrowser.open(url,new=new)
