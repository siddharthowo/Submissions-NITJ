#Write Python program to demonstrate the use of looping statement
n=int(input("Enter number:"))
s=0
while(n):
    d=n%10
    s+=d
    n=n//10
print("Sum of digits of the number:",s)