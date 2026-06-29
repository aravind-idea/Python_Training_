arr = list(map(int, input("Enter numbers: ").split()))
# found=0
# l=len(arr)
# for i in range (l):
#     for j in range(i+1,l):
#         if arr[i]==arr[j]:
#            found=1
# if found==1:
#     print("TRUE")
# else:print("FALSE")
s=set(arr)
l=len(s)
f=len(arr)
if l==f:
    print("False")
else:
    print("True")