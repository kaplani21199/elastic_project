
import io 
import glob
import string 

with open('06_1.xml', 'r', encoding='windows-1255') as file:
	data = file.read()
data = data.replace('"id=', 'id="')
print(data)



#san_check = tostring(div, encoding='unicode')

#print(clean)
