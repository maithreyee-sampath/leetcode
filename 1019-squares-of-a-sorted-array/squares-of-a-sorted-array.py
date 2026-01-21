class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        res = [0]*(len(nums))
        j = len(res)-1

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                res[j]= nums[right] * nums[right]
                right-=1
                j-=1
            else:
                res[j]= nums[left]*nums[left]
                left+=1
                j-=1

    
        return res

