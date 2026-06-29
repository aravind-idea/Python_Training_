a=int(input("enter1"))
b=int(input("enter2"))
c=int(input("enter3"))
d=int(input("enter4"))
if a>=b and a>=c and a>=d:
    print("a greater")
elif b>=a and b>=c and b>=d:
    print("b greater")
elif c>=d:
    print("cgreater")
else:
    print("d greater")