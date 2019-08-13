#file call and inport function 
from UpdateFile import upp
from UniqueCodeFile import unicode
from ReadFile import inv
import datetime

# Define functio to display
def disp (l):  
    cart=[]
    print("\n")
    print("Inventory")
    print("--------------------------------------")
    for i in range (len(l)):
        print(l[i][0],"\t",l[i][1],"\t",l[i][2])
    
    print("--------------------------------------")
    
    ans="y"
    while ans == "y":
        
        j=True
        while j:
            #ask the user to input the name of produc.
            p=input("what product you want? ")
            for i in range(len(l)):
                #check the product available or not in the list.
                if p in l[i]:
                    while True:
                        try:
                            #ask the user to input the number of produc.
                            q=int(input("How many buy product? "))
                        except:
                            print("Sorry! Invalid Input, quantity must be in integer value")
                            continue
                        #check the product in the range.
                        if q<=int(l[i][2]):
                            if len(cart)<=0:
                                cart.append([p,q,l[i][1]])
                            else:
                                incart = True
                                for ii in range(len(cart)):
                                    if p in cart[ii]:
                                        cart[ii][1] = cart[ii][1] + q
                                        incart = False
                                if incart:
                                    cart.append([p,q,l[i][1]]) 
                            while True:
                                #ask the user for continue shopping.
                                ans=input("Do you continue shopping? (y/n): ")
                                if ans=="y"or ans=="n":
                                    break
                                else:
                                    print('Invalid')
                            break
                        else:
                            print("Sorry! The product is out of range")
                    
                    j=False
                    
            if j == True:
                print("Sorry! Invalid Input")
               
    return cart
while True:
    cart=disp(inv())
    #input user name.
    c = input("enter your name: ")
    #call function unicode from UniqueCode.py module.
    cod = unicode()
    print('\n')
    S="===========================================================================\n"
    S = S+"\t\t\t  *NEWA ELECTRONIC STORE* \n"
    S = S+"\t\t   Ghattekulo-29,Anamnagar,Kathmandu \n"
    S = S+"\t\t\t Phone:9867141715 \n\n"
    S = S+str (datetime.datetime.now())+"\n\n"
    S = S+"Name of Customer: "+c+"\n"
    S = S+"\t\t\t\t\t\t Unique Code: "+cod+'\n'
    S = S+"---------------------------------------------------------------------------\n"
    S = S+"Product\tunit Price\tQuantity\tPrice\tDiscount\tTotal Price\n"
    S = S+"---------------------------------------------------------------------------\n"
    net=0
    for i  in range (len(cart)):
        mult=int(cart[i][2])*int(cart[i][1])
        S = S+cart[i][0]+'\t'+str(cart[i][2])+'\t\t'+str(cart[i][1])+'\t\t'+str(mult)+'\t10%\t\t'+str(mult-(mult*10/100))+"\n"
        net=net+(mult-((mult*10/100)))#calculate the total amout.
    S=S+"===========================================================================\n"
    S = S+"\t\t\t\t\t\t   Net Total:   "+str(net)+"\n"
    S = S+'\n\n\t\t  Thankyou for purchasing from us\n\t\t\t Have a nice Day'
    print(S)
    f=open('receipt\ '+c+'-'+cod+'.txt','w') 
    f.write(S)
    f.close()
    upp(cart)

    #ask the user to quit the shopping.
    qui=input('Do you quit the shopping?(y/n):')
    if qui=='n':
        continue
    elif qui=='y':
        break
    else:
        print('invlaid input')
            

                        

        


    
    
    
    


