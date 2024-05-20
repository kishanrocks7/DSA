class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, n):
            current_sum += nums[i]
            if current_sum < nums[i]:
                current_sum = nums[i]
            if max_sum < current_sum:
                max_sum = current_sum
        return max_sum
