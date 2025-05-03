from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'


class Solution:
    def merge_lists(self, l1, l2):
        node = ListNode()
        ans = node

        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next

        if l1:
            node.next = l1
        else:
            node.next = l2

        return ans.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))
            lists = temp

        return lists[0]


    def mergeKListsHehehe(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        working_list = []
        for list_node in lists:
            if list_node is None or list_node == []:
                continue
            while list_node.next is not None:
                working_list.append(list_node.val)
                list_node = list_node.next
            working_list.append(list_node.val)
        working_list.sort()

        if len(working_list) == 0:
            return None

        output_list_nodes = []
        output_list_nodes.append(ListNode(working_list[-1], None))
        for i in range(len(working_list) - 2, -1, -1):
            output_list_nodes.append(ListNode(working_list[i], output_list_nodes[-1]))
        output_list_nodes = output_list_nodes[::-1]

        return output_list_nodes[0]


def createNodesList(lst: list) -> ListNode:
    if len(lst) == 0:
        return []
    output_list = []
    output_list.append(ListNode(lst[-1], None))
    for i in range(len(lst) - 2, -1, -1):
        output_list.append(ListNode(lst[i], output_list[-1]))
    output_list = output_list[::-1]
    return output_list[0]


if __name__ == '__main__':
    solution = Solution()

    lists = [createNodesList([1,4,5]), createNodesList([1,3,4]), createNodesList([2,6])]
    sol = solution.mergeKLists(lists)
    print(sol) # [1,1,2,3,4,4,5,6]

    lists = []
    sol = solution.mergeKLists(lists)
    print(sol) # []

    lists = [createNodesList([])]
    sol = solution.mergeKLists(lists)
    print(sol) # []
