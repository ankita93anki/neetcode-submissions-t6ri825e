class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = []
        for i in range(len(nums)):
            if nums[i] in result:
                return True
            result.append(nums[i])
        return False
        