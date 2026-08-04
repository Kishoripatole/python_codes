a=int(input("enter the number:"))
a1=a//1000
a2=(a//100)%10
a3=(a//10)%10
a4=(a%1000)


rev=(a4*1000)+(a3*100)+(a2*10)+a1

if rev==a:
    print("Number is armstrong.")
else:
    print("Not armstrong.")