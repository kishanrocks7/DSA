class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ind=-1
        l=len(nums)
        for i in range(l-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            nums.sort()
            return None

        for i in range(l-1,ind,-1):
            if(nums[ind]<nums[i]):
                temp=nums[i]
                nums[i]=nums[ind]
                nums[ind]=temp
                break
        nums[ind+1:l]=sorted(nums[ind+1:l])
            
                        
