print("All the elements with Celsius value:")
print("celsius= ",end="")
celsius=[10,20,31.3,40,39.2]
print(celsius)
print(" Celsius to Fahrenheit Conversion ")
print("Fahrenheit = ",end="")
Fahrenheit=[((float(9)/5)*x + 32) for x in celsius]
print(Fahrenheit)
