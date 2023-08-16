#def displayUser(*args):       #tuple
#    print(type(args))
#    print(args)

#displayUser()

def displayUser(**kwargs):                 #dictionary
    for  key,value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")                   
    
displayUser(username= "bartuakdogan")    
displayUser(username= "bartuakdogan", email= "info@bartuakdogan.com")
displayUser(username= "bartuakdogan",email= "info@bartuakdogan.com",country= "Turkey")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,70,key1="value1",key2="value2")    