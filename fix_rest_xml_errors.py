#corrects non-printable characters 
import io 
import glob
import xml.etree.ElementTree as ET
import string
import unicodedata, re, itertools, sys

# or equivalently and much more efficiently
control_chars = b''.join(map(bytes, itertools.chain(range(0x00,0x20), range(0x7f,0xa0))))
control_char_re = re.compile(b'[%s]' % re.escape(control_chars))

def remove_control_chars(s):
    return control_char_re.sub(b'', s)

def replace_and_chars(fname):
    outbuffer = []
    f = open(fname,"rb")
    file_buffer_contents = f.read().split(b'\n')
    for l in range(len(file_buffer_contents)):
        file_buffer_contents[l] = remove_control_chars(file_buffer_contents[l])
        file_buffer_contents[l] = file_buffer_contents[l].replace(b'\x26',b'\\x26')
        outbuffer.append(file_buffer_contents[l])
    fout = open(fname.replace(".xml","") + "replaced.xml","wb+")
    for l in file_buffer_contents:
        fout.write(l + b'\n')
    fout.close()
    f.close() 
    
    
past = replace_and_chars("./new1.xml")
