a=int(input("enter the 1st number "))
s=input("input the operator as[+,-,*,/,%]")
if(s!="%"):
    b=int(input("enter the 2nd number "))
    if(s=="+"):
        a=a+b
        print("result="+str(a))
    elif(s=="-"):
        a=a-b
        print("result="+str(a))
    elif(s=="*"):
        a=a*b
        print("result="+str(a))
    elif(s=="/"):
        a=int(a/b)
        print("result="+str(a))
else:
    a=a/100
    print("result="+str(a))
        
        
        
        enter the 1st number 10
input the operator as[+,-,*,/,%]+
enter the 2nd number 50
result=60
