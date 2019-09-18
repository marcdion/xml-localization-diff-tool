from xml.dom import minidom

nodetitle = 'text'

#parsing files to compare them. file location will be static for the moment
src = minidom.parse(r'C:\Users\marc-\Desktop\dev\superteck-app\src\Superteck.Core\Localization\SourceFiles\Superteck.xml')
comp = minidom.parse(r'C:\Users\marc-\Desktop\dev\superteck-app\src\Superteck.Core\Localization\SourceFiles\Superteck-fr.xml')

#fetching localization items in both xml files
itemlistsrc = src.getElementsByTagName(nodetitle)
itemlistcomp = comp.getElementsByTagName(nodetitle)

print(len(itemlistsrc))
print(len(itemlistcomp))