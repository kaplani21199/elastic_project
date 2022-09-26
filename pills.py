from xml.etree import ElementTree
import json
import ndjson

nd_data = open("data_correct.ndjson", 'w')

fndjson = ndjson.writer(nd_data)

#with open("nd_data.json", 'w+') as fp:
    #file_contents = json.load(fp) #exw to json periexomeno

tree = ElementTree.parse("06_1replaced.xml")
root = tree.getroot()
name = root.find("name").text
austlii = root.find("AustLII").text


fndjson.writerow([name])
fndjson.writerow([austlii])
catchphrases = root.find("catchphrases")
fndjson.writerow(["id","catchphrase"])
for catchphrase in catchphrases:
    fndjson.writerow([catchphrase.attrib.get('id'),catchphrase.text])
sentences = root.find("sentences")

fndjson.writerow(["id","sentence"])
for sentence in sentences:
    fndjson.writerow([sentence.attrib.get('id'),sentence.text])

