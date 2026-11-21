class KthLargest:
    # [4, 3, 2, 1, 4]
    #  0  1  2  3  4
    # left child = (index * 2) + 1
    # right child = (index * 2) + 2
    # parent of a node = (index - 1) // 2

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.limit = k
        for num in nums:
            self.add(num)
        
        print("INIT MIN_HEAP: ", self.min_heap)
        
    # we wanna keep adding large numbers, larger than the ones in our min heap.
    def add(self, val: int) -> int:
        self.min_heap.append(val)
        index_of_val = len(self.min_heap) - 1
        self.bubbleUp(index_of_val)

        # if we exceed the limit, the minheap makes it so that
        # we have the smallest element at the root, we can kick it out
        # to keep the largest numbers. The root afterwards will always be the kth largest,
        # or the smallest in the group of K.
        if (len(self.min_heap) > self.limit):
            self.popleft()
        
        return self.min_heap[0]
    
    def popleft(self):
        if not self.min_heap: return
        if len(self.min_heap) == 1: return self.min_heap.pop()

        # swap root with the last element (large), pop it, and bubble it down.
        root = self.min_heap[0]
        self.min_heap[0] = self.min_heap.pop()
        self.bubbleDown(0)
        return root

    # [4, 5, 1] -> [1, 5, 4] -> add 10 -> [1, 5, 4, 10]
    def bubbleUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.min_heap[parent] > self.min_heap[i]:
            tmp = self.min_heap[parent]
            self.min_heap[parent] = self.min_heap[i]
            self.min_heap[i] = tmp
            i = parent
            parent = (i - 1) // 2
    
    # example: [10, 4, 5]
    def bubbleDown(self, i):
        size = len(self.min_heap)
        while True:
            smallest = i
            left = (i*2) + 1
            right = (i*2) + 2

            if left < size and self.min_heap[left] < self.min_heap[smallest]:
                smallest = left
            
            if right < size and self.min_heap[right] < self.min_heap[smallest]:
                smallest = right
            
            # if we have found a smaller element, swap the current element with it.
            if smallest != i:
                self.min_heap[i], self.min_heap[smallest] = self.min_heap[smallest], self.min_heap[i]
                i = smallest
            else:
                break
            



        

        
    









