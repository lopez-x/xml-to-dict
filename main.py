import xml.etree.ElementTree as ET
import xmltodict

# clean and parse xml file
tree = ET.parse('books.xml')
root = tree.getroot()

for title in root.findall("book/title"):
    title.attrib.pop('lang', None)

for book in root.findall("book"):
    value = book.get('category')
    book.tag = book.tag + "_" + value
    book.attrib.pop('category', None)

tree.write('output.xml')


with open('output.xml', 'r', encoding='utf-8') as file:
    my_xml = file.read()
my_dict = xmltodict.parse(my_xml, cdata_key='text')
print(my_dict)
