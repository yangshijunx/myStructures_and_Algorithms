# 两数之和
nums = [2,7,11,15]
target = 9
def twoNumSumMethod1(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []
print(twoNumSumMethod1(nums,target))