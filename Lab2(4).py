import io
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys


''' Program read text from the file and append it to xml file.
    Writes all words that have same ending, their column,row and tuple '''

def prefy(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


f = open("a.txt", 'r')

text = f.read()

f.close()

text = re.sub("[,.;]", "", text)

text2 = text.split('\n')

tree = ET.parse('test2.xml')

root = tree.getroot()

ends = ET.SubElement(root, 'ends')

used = []
bool = False

for i, ryadok in enumerate(text2):
    for j, slovo in enumerate(ryadok.split()):
        if len(slovo) >= 3:
            end = re.findall(r'\w..\b', slovo)
            bool = False

            for zakin in used:
                if zakin == end:
                    bool = True

            if bool == True:
                continue

            b = ET.SubElement(ends, 'end')
            b.set('name', str(end))

            used.append(end)
            for g,k in enumerate(text2):
                for h,l in enumerate(k.split()):
                    check = re.findall(r'\w..\b', l)
                    if check == end:
                        q = ET.SubElement(b, 'details')
                        q.set(u"slovo", l)
                        q.set(u'tuple', tuple(l))
                        q.set(u'nomer', str(h + 1))
                        q.set(u'ryadok', str(g + 1))


text = re.sub("[,.]", "", text)

a = text.split()

root.append(ends)

tree.write('test4.xml', encoding='utf-8')

