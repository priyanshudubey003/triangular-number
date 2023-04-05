def cal_factorial(num):
    fact=1
    print(" Entered Number is: ",num)
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of a number",num,"is=",fact)
number=int(input("Enter the Number:"))
cal_factorial(number)
