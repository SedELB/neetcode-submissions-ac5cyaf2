class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for _ in range(k):
            toAdd = max(freq, key=freq.get)
            output.append(toAdd)
            del freq[toAdd]

        return output


