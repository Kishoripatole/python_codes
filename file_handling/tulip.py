
n=int(input("enter the number:"))
n1=n//100
n2=(n//10)%10
n3=(n%100)%10
rev=(n3*100)+(n2*10)+n1
if n==rev:
    print("Number is palindrome.")

else:
    print("Not palindrome .")
 