class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        longestLength = 0
        for num in nums:
            hashmap[num] = False
        
        for num in nums:
            currentLength = 1
            nextNum = num + 1
            while nextNum in hashmap and not hashmap[nextNum]:
                currentLength +=1
                hashmap[nextNum] = True
                nextNum += 1
            
            prevNum = num - 1
            while prevNum in hashmap and not hashmap[prevNum]:
                currentLength += 1
                hashmap[prevNum] = True
                prevNum -= 1
            
            longestLength = max(currentLength, longestLength)
        
        return longestLength
