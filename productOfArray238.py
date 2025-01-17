from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(0, len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer


# Test Cases
sol = Solution()
# # Expected: [24,12,8,6]
print(sol.productExceptSelf([1,2,3,4]))
# # Expected: [0,0,9,0,0]
print(sol.productExceptSelf([-1,1,0,-3,3]))
# # Expected: [0,0,0,0]
# print(sol.productExceptSelf([0,0,0,0]))
