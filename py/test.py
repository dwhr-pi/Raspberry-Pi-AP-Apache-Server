#!/usr/bin/env python
import cgi

data = cgi.FieldStorage()
print "Content-Type: text/html"
print
print data["a"]
