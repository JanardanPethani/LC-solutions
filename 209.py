nums = [2,3,1,2,4,3]
target = 7
# initialize pointers and sum
left, right, total = 0, 0, 0
# initialize minimum length to be the length of the array plus 1 (invalid)
min_len = len(nums) + 1

# loop through the array
while right < len(nums):
    # add current number to the sum
    total += nums[right]
    # move right pointer
    right += 1
    
    # check if the sum is greater than or equal to target
    while total >= target:
        # update minimum length if necessary
        min_len = min(min_len, right - left)
        # subtract left number from the sum and move left pointer
        total -= nums[left]
        left += 1

# if minimum length is still the initialized value, there is no valid subarray
if min_len == len(nums) + 1:
    print(0)
else:
    print(min_len)