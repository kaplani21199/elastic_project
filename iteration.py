import io
import glob
import string
import os
import shutil

# assign directory
directory = '/home/caplani/Desktop/corpus/fulltext'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    # checking if it is a file
    if os.path.isfile(f):
            with open(f, 'r', encoding='windows-1255') as file:
                data = file.read()
                data = data.replace('"id=', 'id="')
                os.system("mv /home/caplani/Desktop/corpus/fulltext/* /home/caplani/Desktop/corpus/id")
                #print(data)
                #break;
