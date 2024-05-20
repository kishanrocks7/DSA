class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')  
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        return max_sum


"""LOGIC: initialize maxsum to least possible value i.e -infinity , now start iteration fromi= 0 to n and inside there
another iteration with j from i to n. This will cover every possible sunsequet array psssible.
No befor j iteration  make current sum=0 as we have already stored maxsum of last iteration.
hence for all iteration we will get our max sum"""