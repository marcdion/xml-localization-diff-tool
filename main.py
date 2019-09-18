#!/usr/bin/python
import sys
from xml.dom import minidom

nodetitle = 'text'

#parsing files to compare them. file location will be static for the moment
src = minidom.parse(str(sys.argv[1]))
comp = minidom.parse(str(sys.argv[2]))

#fetching localization items in both xml files
itemlistsrc = src.getElementsByTagName(nodetitle)
itemlistcomp = comp.getElementsByTagName(nodetitle)

print(len(itemlistsrc))
print(len(itemlistcomp))