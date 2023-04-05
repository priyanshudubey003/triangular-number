num=int(input("Enter the number:"))
fact=1
ans=1
while fact<=num:
    ans=ans*fact
    fact=fact+1
print("Factorial of",num," is:",ans)