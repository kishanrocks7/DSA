class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        zero = 0
        one = 0
        two = 0

        for i in range(0, n):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            elif nums[i] == 2:
                two += 1
        
        for i in range(0, zero):
            nums[i] = 0
        for i in range(zero, zero + one):
            nums[i] = 1
        for i in range(zero + one, n):
            nums[i] = 2


"""LOGIC: Count number of 0,1 & 2 in array. Put that many in nums array inn sorted ssequence."""