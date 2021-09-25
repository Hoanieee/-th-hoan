import math
a = float(input(""))
b = float(input(""))
c = float(input(""))
if(a == 0):
    if(b == 0):
        print("Phương trình vô nghiệm!");
    else:
        print("Phương trình có nghiệm duy nhất: x =", + (-c/b));
delta = b * b - 4 * a * c
if delta > 0:
    x1 = (float)