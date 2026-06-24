class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums) #cant initialize it to 0 since we can have neg numbers too

        curr_min, curr_max = 1, 1

        for n in nums:
            if n is 0:
                curr_min, curr_max = 1, 1
                continue
            
            temp = n * curr_max
            curr_max = max(n * curr_max, n * curr_min, n) #[-1,8]
            curr_min = min(temp, n * curr_min, n) ##[-1,-8]

            res = max(res, curr_max)
            
        return res