import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        ele1 = 0
        ele2 = 0
        cnt2 = 0
        n = len(nums)
        threshold = math.floor(n/3)
        for i in range(len(nums)):
            if cnt1 == 0  and nums[i] != ele2:
                cnt1 = 1
                ele1 = nums[i]
            elif cnt2 == 0 and nums[i] != ele1:
                cnt2 = 1
                ele2 = nums[i]
            elif nums[i] == ele1:
                cnt1 += 1
            elif nums[i] == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1
        ls = []
        if cnt1 > threshold:
            ls.append(ele1)
        if cnt2 > threshold:
            ls.append(ele2)
        return ls