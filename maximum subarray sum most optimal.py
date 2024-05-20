class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        max_sum=nums[0]
        n=len(nums)
        for i in range(1,n):
            sum=sum+nums[i]
            if sum<nums[i]:
                sum=nums[i]
            if sum>max_sum:
                max_sum=sum
            
            
        
        return max_sum
            

"""LOGIC: initialize two varable sum and maxsum with nums[0] now iterate array from 1 to n.
while iterating it add ith element to sum if sum < ith elelmet make sum= ith element ( why to carry negative burden)
next compare with maxsum if sum>maxsum make maxsum=sum. Thats all"""