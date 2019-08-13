#define function to generate uniquecode.

import string
from random import randint
def unicode():
    a = string.ascii_lowercase
    
    while True:
        c=""
        for i in range (6):
            c=c+a[randint(0,25)]
        #read ucode.txt file to check previously use code.    
        file = open('Ucode.txt','r')
        li = file.read().split('\n')
        file.close()
        if c not in li:
            #add newly generated code to file.
            file=open('Ucode.txt','w')
            file.write('\n'.join(li) +'\n'+c)            
            break
        else: continue
    return c

