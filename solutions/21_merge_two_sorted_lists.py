from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createNodesList(lst: list) -> ListNode:
    if len(lst) == 0:
        return None
    curr_list_node = ListNode(lst[-1], None)
    for i in range(len(lst) - 2, -1, -1):
        curr_list_node = ListNode(lst[i], curr_list_node)
    return curr_list_node


def getNormalListFromHead(head) -> list[int]:
    output = []
    curr = head
    if curr is None:
        return []
    while curr:
        output.append(curr.val)
        curr = curr.next
    return output


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        list_node_0 = ListNode()
        curr_list_node = list_node_0

        while p1 and p2:
            if p1.val < p2.val:
                curr_list_node.next = p1
                p1 = p1.next
            else:
                curr_list_node.next = p2
                p2 = p2.next

            curr_list_node = curr_list_node.next

        if p1:
            curr_list_node.next = p1
        else:
            curr_list_node.next = p2

        return list_node_0.next

    def mergeTwoListsCheat(self, list1: Optional[ListNode],
                           list2: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                output.append(p1.val)
                p1 = p1.next
            else:
                output.append(p2.val)
                p2 = p2.next

        if not p1:
            while p2:
                output.append(p2.val)
                p2 = p2.next
        else:
            while p1:
                output.append(p1.val)
                p1 = p1.next

        if len(output) == 0:
            return None
        curr_list_node = ListNode(output[-1], None)
        for i in range(len(output) - 2, -1, -1):
            curr_list_node = ListNode(output[i], curr_list_node)

        return curr_list_node


if __name__ == '__main__':
    solution = Solution()

    list1 = createNodesList([1,2,4])
    list2 = createNodesList([1,3,4])
    print(solution.mergeTwoLists(list1, list2)) # [1,1,2,3,4,4]

    list1 = createNodesList([])
    list2 = createNodesList([])
    print(solution.mergeTwoLists(list1, list2)) # []

    list1 = createNodesList([])
    list2 = createNodesList([0])
    print(solution.mergeTwoLists(list1, list2)) # [0]
