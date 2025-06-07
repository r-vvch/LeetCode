class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return str(self.val)


class Solution:
    # O(n), O(n)
    def lowestCommonAncestorSet(self, p: Node, q: Node) -> Node:
        nodes_set = set()
        node = p
        while node:
            nodes_set.add(node)
            node = node.parent
        node = q
        while node not in nodes_set:
            node = node.parent
        return node

    # O(n), O(1)
    def lowestCommonAncestorPointers(self, p: Node, q: Node) -> Node:
        a, b = p, q
        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p
        return a

    lowestCommonAncestor = lowestCommonAncestorPointers


if __name__ == '__main__':
    solution = Solution()

    tn_7 = Node(7, None, None)
    tn_4 = Node(4, None, None)
    tn_2 = Node(2, tn_7, tn_4)
    tn_6 = Node(6, None, None)
    tn_5 = Node(5, tn_6, tn_2)
    tn_0 = Node(0, None, None)
    tn_8 = Node(8, None, None)
    tn_1 = Node(1, tn_0, tn_8)
    tn_3 = Node(3, tn_5, tn_1)

    tn_7.parent = tn_2
    tn_4.parent = tn_2
    tn_6.parent = tn_5
    tn_2.parent = tn_5
    tn_0.parent = tn_1
    tn_8.parent = tn_1
    tn_5.parent = tn_3
    tn_1.parent = tn_3

    p = tn_5
    q = tn_1
    print(solution.lowestCommonAncestor(p, q)) # 3

    p = tn_5
    q = tn_4
    print(solution.lowestCommonAncestor(p, q)) # 5


    tn_2 = Node(2, None, None, None)
    tn_1 = Node(1, tn_2, None, None)
    tn_2.parent = tn_1

    p = tn_1
    q = tn_2
    print(solution.lowestCommonAncestor(p, q)) # 1
