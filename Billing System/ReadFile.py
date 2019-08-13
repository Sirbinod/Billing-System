#define inv() function to generate 2d list of inventory.
def inv():
    file=open("store.txt","r")#read file and open
    f=file.read()
    g=f.split()
    l=[]
    
    for i in range (len(g)):
        
        #convert to 2D list
        l.append(g[i].split(","))
        
    return l
    
