# define function to update inventory.
def upp(C):
    li = []

    #read invtory from file.
    file = open('store.txt','r')
    lii = file.read().split('\n')
    for i in lii:
        li.append(i.split(','))
    file.close()
    #updating inventory in list
    for i in range(len(li)):
        for iji in range(len(C)):
            if C[iji][0] in li[i]:
                y = int(li[i][2])-int(C[iji][1])
                li[i][2] = str(y)
    x=[]
    for i in li:
        x.append(','.join(i))
    # writes the updated inventory file.
    file = open('store.txt','w')
    file.write('\n'.join(x))
    file.close()

