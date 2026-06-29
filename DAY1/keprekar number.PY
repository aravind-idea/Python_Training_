N=int(input("input"))
square=N*N
res=square%100
square=square//100
sum=square +res
if sum==N:
    print("keprekar99")
else:
    print("not")