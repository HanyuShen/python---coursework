C= float(input("Please enter a temperature in degress celsius:  "))
F=C*1.8+32
print("The degree in Fahrenheit is:{} ,".format(F))


R=float(input("Please enter the radius of the circle:"))
A=R**2*3.14
C=2*R*3.14
print("The area of the circle is:{}".format(A) , "The circumference of the circle is:{}".format(C))

R=float(input("PLease enter a radius of the sphere:"))
S=4*3.14*R**2
print("The surface of a sphere is :{}".format(S))

R=float(input("Pleaase enter a radius of the cylinder:"))
H=float(input("PLease enter a height of the cylinder:"))
S=R**2*3.14*H
print("The surface area of the cylinder is:{}".format(S))



fn=input("PLease enter your first name:")
sn=input("Please enter your last name:")
F=str(fn[0])
S=str(sn[0])
print(F+S)

age = input("Please enter your age:")
if int(age)>18:
    print(True)
else:
    print(False)
