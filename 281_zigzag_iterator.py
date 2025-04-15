from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.current_vector = 0
        self.vectors = [v1, v2]
        self.indexes = [0] * len(self.vectors)

    def next(self) -> int:
        # shifting to next vector is already made in hasNext,
        # so we just yield needed value and change indexes
        vector = self.vectors[self.current_vector]
        current_element_index = self.indexes[self.current_vector]
        output = vector[current_element_index]
        self.indexes[self.current_vector] = current_element_index + 1
        self.current_vector = (self.current_vector + 1) % len(self.vectors)
        return output

    def hasNext(self) -> bool:
        start_vector = self.current_vector
        # if the current vector is exhausted we move to the next one
        while self.indexes[self.current_vector] == len(self.vectors[self.current_vector]):
            self.current_vector = (self.current_vector + 1) % len(self.vectors)
            # if the other one is exhausted too - we have no more elements left
            if self.current_vector == start_vector:
                return False
        return True


if __name__ == '__main__':
    v1 = [1,2]
    v2 = [3,4,5,6]
    i, v = ZigzagIterator(v1, v2), []
    while i.hasNext():
        v.append(i.next())
        print(v)
    assert v == [1,3,2,4,5,6]
    # Explanation: By calling next repeatedly until hasNext returns false,
    # the order of elements returned by next should be: [1,3,2,4,5,6].

    v1 = [1]
    v2 = []
    i, v = ZigzagIterator(v1, v2), []
    while i.hasNext():
        v.append(i.next())
        print(v)
    assert v == [1]

    v1 = []
    v2 = [1]
    i, v = ZigzagIterator(v1, v2), []
    while i.hasNext():
        v.append(i.next())
        print(v)
    assert v == [1]
