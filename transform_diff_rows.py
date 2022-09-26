
from xml.etree import ElementTree
import csv

csvfile = open("data1.csv",'w')

csvfile_writer = csv.writer(csvfile)
tree = ElementTree.parse("06_1replaced.xml")
root = tree.getroot()

name = root.find("name").text
austlii = root.find("AustLII").text

csvfile_writer.writerow([name])
csvfile_writer.writerow([austlii])
catchphrases = root.find("catchphrases")
csvfile_writer.writerow(["id","catchphrase"])
for catchphrase in catchphrases:
    csvfile_writer.writerow([catchphrase.attrib.get('id'),catchphrase.text])
sentences = root.find("sentences")

csvfile_writer.writerow(["id","sentence"])
for sentence in sentences:
    csvfile_writer.writerow([sentence.attrib.get('id'),sentence.text])
