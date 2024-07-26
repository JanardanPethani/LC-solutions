nums = [-1,0,1,2,-1,-4]
nums.sort()
finalList = []
for idx, ival in enumerate(nums):
    if idx > 0 and ival == nums[idx -1]:
        continue
    
    l ,r = idx + 1, len(nums) - 1
    
    while l < r:
        ans = ival + nums[l] + nums[r]
        if ans > 0:
            r -= 1
        elif ans < 0:
            l += 1
        else:
            finalList.append([ival , nums[l] , nums[r]])
            l += 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1
print(finalList)            