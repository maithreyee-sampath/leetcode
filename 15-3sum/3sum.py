class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #[-1,0,1,2,-1,-4]

        res = [] #empty res list   [-4,-1,-1,0,1,2]
        nums.sort() #sort it        i  l       r

        for i in range(len(nums)):
            if i !=0 and nums[i] == nums[i-1]:  # edge case: where i is checked for duplicates
                continue
            
            # 2 sum on the remainder of list
            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -=1
                elif total < 0:
                    l +=1
                else:
                    res.append([nums[i], nums[l], nums[r]]) #appended res if sum is 0
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
        return res
