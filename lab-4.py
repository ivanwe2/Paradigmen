a = 5
b = 4

if(a==b):
   b=1
else:
   b=2
   b=6
##dava vadi 6

   
if(a==b):
    pass #skipva reda a ako e prazno kompilativna greshka
else:
    b=2
    b=6

################3

while(True):
    n=input("Enter age:\n")
    if(n.isdigit()):
        n=int(n)
        break
else:
    print("watafak choek loops have an else")


if (n<0 or n>151):
    print("invalid age")
elif(n<18):
    print("age limit is 18")
else:
    print("you are free to proceed")


###########domashna
    ####kyv e smisyla na else clausa na cikli watafak sh go zabraq ngl
    ####https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
    ##pyrvi otgovor

