def factotial(n):
    if n==0:
        return 1
    return n*factotial(n-1)
print(factotial(5))