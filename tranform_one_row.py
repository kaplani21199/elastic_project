#transform into one row csv file
from xml.etree import ElementTree
import csv

csvfile = open("data.csv",'w')

csvfile_writer = csv.writer(csvfile)
tree = ElementTree.parse("06_1replaced.xml")
root = tree.getroot()

csvfile_writer.writerow(["name","AustLII","catchphrases","sentences"])

name = root.find("name").text
austlii = root.find("AustLII").text
catchphrasesAll = ""
sentencesAll = ""
catchphrases = root.find("catchphrases")
for catchphrase in catchphrases:
    catchphrasesAll += catchphrase.attrib.get('id') + " " + catchphrase.text + "\n"
sentences = root.find("sentences")
for sentence in sentences:
    sentencesAll += sentence.attrib.get('id') + " " + sentence.text + "\n"

csvfile_writer.writerow([name,austlii,catchphrasesAll,sentencesAll])
