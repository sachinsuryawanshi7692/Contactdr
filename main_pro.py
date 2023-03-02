'''
Main file
'''
def validdate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0
def create_contact():
    f=open('data.txt','a')
    n=input("Enter the Name:")
    mn=input("Enter the Mobile Number:")
    res=validdate_mob(mn)
    if res==1:
        a,b=searchmob(mn)
        if b==1:
            print("Number already exit:")
        else:
       
          d=n+":"+mn+"\n"
          f.write(d)
          f.close()
          print("Contact create Successfully!!!")
    else:
       print("Please valid Number:")
    
def display():
    f=open('data.txt','r')
    d=f.read()
    print("========Contact directory=======")
    print()
    print(d)
    print("=========================")

def searchmob(n):
          
        
        f=open('data.txt','r')
        data=f.readlines()
        
        for x in data:
            l=x.split(":")
            if int(n)==int(l[1]):
                #print("Contact found:")
                #print(x)
                
                return x,1
                 
        else:
                return '',0

def searchname():
        print("Search contact Number by Name:") 
        ns=input("Enter Name:")
        f=open('data.txt','r')
        data=f.readlines()
        print(data)
        for x in data:
            #print(x)
             l=x.split(":")
             #print(l)
             #print(l[0])
             if ns.upper()==l[0].upper():
                 print(x)
                 flag=1
                 
        if flag==0:
            print("Contact Not Found")
            
        f.close()
        
    
            
           
    
print("Welcome to contact Directory console Application")
print()
while True:
    print("1.Create Contact")
    print("2.View Contact")
    print("3.Search by name")
    print("4.Search by mobile Number")
    print("5.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        create_contact()
    elif ch==2:
        display()
    elif ch==3:
        searchname()
        
    elif ch==4:
        ms=int(input("Search contact mobile by Number:"))
        a,b=searchmob(ms)
        print(a)
        print(b)
        if b==1:
            print("Contact Found:")
            print(a)
        else:
            print("NOT FOUND")
           
    elif ch==5:
        break
    else:
        print("Sudhar jayo: please enter valid option!!!")
print("Thank u for using Application")        
