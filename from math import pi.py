from Math import pi
Radius=eval(input("Enter Radius Of Circle: "))
if Radius>0:
    Area=Radius*Radius*pi
    print(" Area of Circle is = ",format(Area,".2f"))
    circumference=2*pi*Radius
    print("Circumference of Circle is = ",format(circumference,".2f"))