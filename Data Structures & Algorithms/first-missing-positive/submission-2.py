class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains1 = False
        for i in range(len(nums)):
            if nums[i] == 1:
                contains1 = True

            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
            
        if contains1 == False:
            return 1

        for i in range(len(nums)):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0:
                continue
            nums[idx]*= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1

        return n+1        