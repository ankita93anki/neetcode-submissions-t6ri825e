class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) < 3:
            return []
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            while start < end:
                target = nums[i]+nums[start]+nums[end]
                if target == 0:
                    result.add((nums[i],nums[start],nums[end]))
                    start += 1
                    end -= 1
                elif target > 0:
                    end -= 1
                else:
                    start += 1
        
        return list(map(list,result))
            
        