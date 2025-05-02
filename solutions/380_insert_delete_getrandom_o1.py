import random


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.indexes = {}

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.arr.append(val)
        self.indexes[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        idx = self.indexes[val]
        self.arr[idx] = self.arr[-1]
        self.indexes[self.arr[-1]] = idx
        self.arr.pop()
        del self.indexes[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


class RandomizedSetUnoptimal:
    def __init__(self):
        self.set_ = set()

    def insert(self, val: int) -> bool:
        if val not in self.set_:
            self.set_.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.set_:
            self.set_.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.set_))


if __name__ == '__main__':
    randomizedSet  = RandomizedSet()

    # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    print(randomizedSet.insert(1)) # True

    # Returns false as 2 does not exist in the set.
    print(randomizedSet.remove(2)) # False

    # Inserts 2 to the set, returns true. Set now contains [1,2].
    print(randomizedSet.insert(2)) # True

    # getRandom() should return either 1 or 2 randomly.
    print(randomizedSet.getRandom()) # 2

    # Removes 1 from the set, returns true. Set now contains [2].
    print(randomizedSet.remove(1)) # True

    # 2 was already in the set, so return false.
    print(randomizedSet.insert(2)) # False

    # Since 2 is the only number in the set, getRandom() will always return 2.
    print(randomizedSet.getRandom()) # 2


    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(0)) # [0]
    print(randomizedSet.insert(1)) # [0, 1]
    print(randomizedSet.remove(0)) # [1]
    print(randomizedSet.insert(2)) # [1, 2]
    print(randomizedSet.remove(1)) # [2]
    print(randomizedSet.getRandom())
