class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hashmap = {}
        def get_frequency_string(element):
            freq_list = [0] * 26
            for char in element:
                freq_list[ord(char)-ord('a')] += 1
            frequency_string = []
            char = 'a'
            for position in freq_list:
                frequency_string.append(char)
                frequency_string.append(str(position))
                char = chr(ord(char)+1)
            return ''.join(frequency_string)
        
        for element in strs:
            frequency_string = get_frequency_string(element)
            if frequency_string not in hashmap:
                hashmap[frequency_string] = []
            hashmap[frequency_string].append(element)
        return list(hashmap.values())
