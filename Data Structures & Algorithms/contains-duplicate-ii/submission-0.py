class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = {}
        for i in range(len(nums)):
            if nums[i] in result :
                if i - result[nums[i]] <= k:
                    return True
            result[nums[i]] = i
        return False

        