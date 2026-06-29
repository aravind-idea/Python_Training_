prorductID=list(map(int,input("Enter The Number").split()))
all_ids=set(prorductID)
duplicates=set()
for i in prorductID:
    if prorductID.count(i)>1:
        duplicates.add(i)                                
lost_ids=all_ids-duplicates
print("Lst Product IDs:",lost_ids)