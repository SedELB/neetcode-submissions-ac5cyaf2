class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                # we go on to the next substring
                l = max(hashmap[s[r]] + 1, l)
            
            # as long as we arent interrupted, we update the res
            hashmap[s[r]] = r
            res = max(res, r - l + 1)

        return res

        # "zxyzxyz"
        # hashmap = {'z': 0, 'x': 1, 'y': 2}