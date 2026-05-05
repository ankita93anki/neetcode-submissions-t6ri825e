class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num]+=1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for key,freq in hashmap.items():
            bucket[freq].append(key)
        
        result = []
        for i in reversed(range(len(bucket))):
            if bucket[i]:
                for value in bucket[i]:
                        result.append(value)
                        if len(result) ==k:
                            return result
        return result

        