class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # contains {key: Node(key, val)}
        self.capacity_used = 0
        self.capacity = capacity

        self.head = Node(0, 0) # dummy!
        self.tail = Node(0, 0) # dummy!
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node: Node):
        # insert a value just before the tail.
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node) # removing it from its current position
            self._insert(node) # re-inserting it as MRU.
            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if we are updating, we need to delete and reinsert to respect its order.
        if key in self.cache:
            self._remove(self.cache[key]) # remove the node

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node) # inserting the new node at the end of the list, making it MRU.

        # after insertion, has the capacity exceeded?
        if len(self.cache) > self.capacity:
            # evict the LRU (head node)
            evicted_node = self.head.next
            self._remove(evicted_node)
            del self.cache[evicted_node.key]










