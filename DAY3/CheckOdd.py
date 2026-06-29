n=list(map(int,input("enter the input").split()))
even=0
odd=0
for i in n:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"{even} even numbers")
print(f"{odd} odd numbers")