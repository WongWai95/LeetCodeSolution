class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.bank = {}
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_bottom(self, key):
        self.bank[key][1].prev.next = self.bank[key][1].next
        self.bank[key][1].next.prev = self.bank[key][1].prev
        self.bank[key][1].prev = self.tail.prev
        self.tail.prev = self.bank[key][1]
        self.bank[key][1].next = self.tail
        self.tail.prev.prev.next = self.bank[key][1]
    
    def _pop_top(self):
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.bank:
            return -1
        self._move_bottom(key)
        return self.bank[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.bank:
            self.bank[key][0] = value
            self._move_bottom(key)
        else:
            if len(self.bank) >= self.capacity:
                self.bank.pop(self.head.next.val)
                self._pop_top()
            cur = Node(key)
            self.bank[key] = [value, cur]
            self.tail.prev.next = cur
            cur.next = self.tail
            cur.prev = self.tail.prev
            self.tail.prev = cur
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)