def longestWindow(nums,k):
    left=0
    maxlen=0
    for right in range(len(nums)):
        while nums[right]-nums[left]>k:
            left+=1
        maxlen=max(maxlen,right-left+1)
    return maxlen
nums=[1,3,5,7,9]
k=4
print(longestWindow(nums,k))