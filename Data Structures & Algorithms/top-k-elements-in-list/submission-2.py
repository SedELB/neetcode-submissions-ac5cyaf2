class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num, count in freq.items():
            buckets[count].append(num)
        
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
    


