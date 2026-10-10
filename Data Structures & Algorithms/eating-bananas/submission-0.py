class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        # [3, 6, 7, 11] h = 8
        we know that the minimum rate k is 1
        we know that the maximum rate k is max(piles) since its useless to go higher.

        we know what the time required for a pile is time = ceil(pile[i] / k)
        and sum of theses times must be >= h.

        so we can try k [1 ... 11] but its O(max(piles) x len(piles))
        but we can apply binary search on [1...11] !
        """

        low = 1 # our lowest k possible
        high = max(piles) # our highest k possible
        k = high
        while low <= high:
            pile_time_to_eat = 0
            mid = low + ((high-low) // 2) # the k we are trying out.

            for i in range(len(piles)):
                pile_time_to_eat += -(-piles[i] // mid) # total time to eat all piles for a given k (mid)
            
            if pile_time_to_eat <= h: # its good.
                k = min(k, mid)
                high = mid - 1 # can we find lower ?
            
            if pile_time_to_eat > h: # its bad
                low = mid + 1  # we must have a higher rate.
        
        return k




