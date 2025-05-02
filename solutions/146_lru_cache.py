class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hist = []
        self.dic = {}

    def get(self, key: int) -> int:
        if key in self.dic:
            self.hist.pop(self.hist.index(key))
            self.hist.append(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
        if key in self.hist:
            self.hist.pop(self.hist.index(key))
        self.hist.append(key)
        if len(self.dic) > self.capacity:
            del self.dic[self.hist[0]]
            self.hist.pop(0)


class LRUCacheFast(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = {}
        self.tail = {}
        self.head['next'] = self.tail
        self.tail['prev'] = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node['val']

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = {'key': key, 'val': value}
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru_node = self.head['next']
            self._remove(lru_node)
            del self.cache[lru_node['key']]

    def _remove(self, node):
        prev = node['prev']
        next = node['next']
        prev['next'] = next
        next['prev'] = prev

    def _add(self, node):
        prev = self.tail['prev']
        prev['next'] = node
        self.tail['prev'] = node
        node['prev'] = prev
        node['next'] = self.tail


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)     # cache is {1=1}
    lRUCache.put(2, 2)     # cache is {1=1, 2=2}
    print(lRUCache.get(1)) # return 1
    # 1
    lRUCache.put(3, 3)     # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2)) # returns -1 (not found)
    # -1
    lRUCache.put(4, 4)     # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1)) # return -1 (not found)
    # -1
    print(lRUCache.get(3)) # return 3
    # 3
    print(lRUCache.get(4)) # return 4
    # 4

    # lRUCache = LRUCache(2)
    # print(lRUCache.get(2))
    # # -1
    # lRUCache.put(2, 6)
    # print(lRUCache.get(1))
    # # -1
    # lRUCache.put(1, 5)
    # lRUCache.put(1, 2)
    # print(lRUCache.get(1))
    # # 2
    # print(lRUCache.get(2))
    # # 6
