from lxml import etree

root = etree.Element('html')

doc = etree.ElementTree(root)

headElt = etree.SubElement(root, 'head')
bodyElt = etree.SubElement(root, 'body')

title = etree.SubElement(headElt, 'title')
title.text = 'Your page title here'

linkElt = etree.SubElement(headElt, 'link', rel='stylesheet',
    href='mystyle.css', type='text/css')

outFile = open('homemade.xml', 'wb')
doc.write(outFile)