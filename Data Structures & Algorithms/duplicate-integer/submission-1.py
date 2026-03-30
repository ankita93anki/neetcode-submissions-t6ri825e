class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        nums.sort()
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return True
        return False