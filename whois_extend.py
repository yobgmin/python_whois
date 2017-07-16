#-*- encoding:utf-8 -*-

import sys
import whois

fname = ''
try:
    fname = sys.argv[1]
except IndexError:
    print "Usage : ./whois_ex [filename]"

fr = open(fname, 'rt')
fw = open('fres.txt', 'w')
data = fr.read()
urllist = data.split()

for x in range(0,len(urllist)):
    a = str(whois.whois(urllist[x]))+'\n' # whois module returns json format itself, so I used it.
    print a
    fw.write(a)

fw.close()
fr.close()
