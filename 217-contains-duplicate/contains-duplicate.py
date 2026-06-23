class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}

        for i in range(len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]] = i
            elif nums[i] in hmap:
                return True
        return False