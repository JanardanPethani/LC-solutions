nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
k = 1

def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    maxSc = 0
    def backtrack(start, comb):
        nonlocal maxSc
        if len(comb) == k:
            calc = sum([nums1[i] for i in comb]) * min([nums2[i] for i in comb])
            if maxSc < calc: 
                maxSc = calc
            return
        
        for i in range(start, len(nums1)):
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()    
    backtrack(0, [])
    return maxSc


print(maxScore(nums1, nums2, k))
