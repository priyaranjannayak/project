x=int(input("enter the1st number"))
y=int(input("enter the 2nd number"))
z=int(input("enter the 3td number"))
if(x>y and x>z):
    print(str(x)+"is grater")
elif(y>x and y>z):
        print(str(y)+"is grater")
else:
    print(str(z)+"is grater")
sum=x+y+z
print("sum of three number is"+str(sum)) 
sum=x
if(y!=x):
    sum=sum+y
if(z!=x and z!=y):
    sum=sum+z
print("sum of non duplicate number is"+str(sum))    


enter the1st number10
enter the 2nd number10
enter the 3td number10
10is grater
sum of three number is30
sum of non duplicate number is10
