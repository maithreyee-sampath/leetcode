class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        hashmap = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in hashmap:
        #         return [hashmap[target-nums[i]], i]
            
        #     hashmap[nums[i]] = i

        for i, n in enumerate(nums):
            if target - n in hashmap:
                return[hashmap[target-n],i]
            
            hashmap[n] = i