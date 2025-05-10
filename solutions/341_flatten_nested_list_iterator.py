# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    # def getList(self) -> [NestedInteger]:
    def getList(self) -> list:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.arr = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.arr.append(nestedList[i])

    def next(self) -> int:
        return self.arr.pop().getInteger()

    def hasNext(self) -> bool:
        # Flatten the list by popping elements from the arr until we find an integer
        while self.arr:
            current = self.arr[-1]
            if current.isInteger():
                return True

            # If it's a list, pop it and push its elements in reverse order
            self.arr.pop()
            nested_list = current.getList()
            for i in range(len(nested_list) - 1, -1, -1):
                self.arr.append(nested_list[i])

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
    nestedList = [[1,1],2,[1,1]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v) # [1,1,2,1,1]

    nestedList = [1,[4,[6]]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v) # [1,4,6]

    # # TESTING
    # ni_int = NestedInteger(1)
    # print(ni_int.isInteger()) # True
    # print(ni_int.getInteger()) # 1
    # print(ni_int.getList()) # None

    # ni_int = NestedInteger([1])
    # print(ni_int.isInteger()) # False
    # print(ni_int.getInteger()) # None
    # print(ni_int.getList()) # [1]
