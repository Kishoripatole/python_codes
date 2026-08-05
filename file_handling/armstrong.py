n=int(input("enter the number:"))
n1=n//1000
n2=(n//100)%10
n3=(n//10)%10
n4=(n%10)
rev=(n3*100)+(n2*10)+n1
one=n1*n1*n1*n1
two=n2*n2*n2*n2
three=n3*n3*n3*n3
four=n4*n4*n4*n4
addition=one+two+three+four
if n==addition:
    print("this is armstrong number!")
else:
    print("this is not armstrong number!")