def main():
    s=input("Enter a string: ").strip
    if isPalidrome(s):
        print(s, "is a palidrome")
    else:
        print(s," is not a palidrome")
# check if a string is a palidrome
def isPalidrome(s):
    low=0
    high=len(s)-1
    while low < high:
        if s[low] != s[high]:
            return False
        low+=1
        high-=1
    return True
main()