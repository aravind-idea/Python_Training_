numbers=list(map(int,input("enter the list:").split()))
k=int(input("enter the threshold value k:"))
freq=dict()

for num in numbers:
    freq[num]=freq.get(num,0)+1

for num,count in freq.items():
    if count>k:
        print(f"{num}:{count} times")
