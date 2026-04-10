class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for string in strs:
            count = [0] * 26 # [0, 0, 0 ... 0]
        
            for char in string:
                count[ord(char) % 26] += 1
                
            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = []
                
            hashmap[key].append(string)
            # { (0,1,0,0): act }
            
        return list(hashmap.values())
        

