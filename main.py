#!/usr/bin/python
import sys
from xml.dom import minidom

nodetitle = sys.argv[1]

#parsing files to compare them. file location will be static for the moment
src = minidom.parse(str(sys.argv[2]))
comp = minidom.parse(str(sys.argv[3]))

#fetching localization items in both xml files
itemlistsrc = src.getElementsByTagName(nodetitle)
itemlistcomp = comp.getElementsByTagName(nodetitle)

print(f'\nSearching nodes matching: {nodetitle}\n')
print(f'Nodes matching descriptor in first file: {len(itemlistsrc)}')
print(f'Nodes matching descriptor in second file: {len(itemlistcomp)}')