class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left_product,right_product = 1,1
        result = nums[0]
        for i in range(n):
            if left_product == 0:
                left_product = 1
            if right_product == 0:
                right_product = 1
            
            left_product = left_product*nums[i]
            right_product = right_product*nums[n-i-1]
            result = max(result, max(left_product, right_product))
        return result
        