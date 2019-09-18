#!/usr/bin/python
import sys
from xml.dom import minidom

nodetitle = sys.argv[1]

#parsing files to compare them. file location will be static for the moment
src = minidom.parse(str(sys.argv[2]))
comp = minidom.parse(str(sys.argv[3]))

#fetching localization items in both xml files
itemListSrc = src.getElementsByTagName(nodetitle)
itemListComp = comp.getElementsByTagName(nodetitle)

itemListSrcValues = []
itemListCompValues = []

print(f'\nSearching nodes matching: {nodetitle}\n')
print(f'Nodes matching descriptor in first file: {len(itemListSrc)}')
print(f'Nodes matching descriptor in second file: {len(itemListComp)}')

for s in itemListSrc:
    itemListSrcValues.append(s.attributes['name'].value)

for c in itemListComp:
    itemListCompValues.append(c.attributes['name'].value)

diff_list_src = list(set(itemListSrcValues)-set(itemListCompValues))
diff_list_comp = list(set(itemListCompValues)-set(itemListSrcValues))

print(f'\nNumber of nodes present in both files: {len(itemListSrc)-len(diff_list_src)}')
print(f'Number of nodes present in first file and missing in second: {len(diff_list_src)}')
print(f'Number of nodes in second file and missing in first: {len(diff_list_comp)}')

print(f'\nNodes present in first file but missing in second:\n')

count_s = 1
for val in diff_list_src:
    print(f'{count_s}. {val}')
    count_s = count_s + 1

print(f'\nNodes present in second file but missing in first:\n')

count_c = 1
for val in diff_list_comp:
    print(f'{count_c}. {val}')
    count_c = count_c + 1