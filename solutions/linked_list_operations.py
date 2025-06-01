"""
Module for work with linked lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createNodesList(lst: list) -> ListNode:
    if len(lst) == 0:
        return []
    curr_list_node = ListNode(lst[-1], None)
    for i in range(len(lst) - 2, -1, -1):
        curr_list_node = ListNode(lst[i], curr_list_node)
    return curr_list_node


def getNormalListFromHead(head: ListNode) -> list[int]:
    output = []
    curr = head
    if curr is None:
        return []
    while curr:
        output.append(curr.val)
        curr = curr.next
    return output
