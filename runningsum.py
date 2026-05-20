def runningsum(nums):
    for i in range(1,len(nums)):
        nums[i] +=nums[i-1]
    return nums
    
nums=list(map(int,input("Enter the array elements seperated by space:").split()))
result=runningsum(nums)
print("running sum of the array is:",result)