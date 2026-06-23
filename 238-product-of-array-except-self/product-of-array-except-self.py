class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        postfix = [0]*len(nums)
        res = [0]*len(nums)
       
        prefix[0] = 1 #first ele prefix will always be 1

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        postfix[-1] = 1 #last ele prefix will always be 1

        for i in range(len(nums)-2,-1,-1):
            postfix[i] =  postfix[i+1] * nums[i+1]

        # res[0] = postfix[0]
        
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        
        # res[-1] = prefix[len(nums)-2]

        return res