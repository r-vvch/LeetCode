from typing import Optional
from linked_list_operations import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        list_len = 1
        while node.next:
            list_len += 1
            node = node.next
        
        if list_len == 1:
            return None

        node = head
        for i in range(list_len - n - 1):
            node = node.next
        
        if n == 1:
            node.next = None
        elif n == list_len:
            # we need to delete the head itself
            head = head.next
        else:
            nth_plus_one_node = node.next.next
            node.next = nth_plus_one_node

        return head

    def removeNthFromEndFast(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next


if __name__ == '__main__':
    solution = Solution()

    head = createNodesList([1,2,3,4,5])
    n = 2
    print(getNormalListFromHead(solution.removeNthFromEnd(head, n))) # [1,2,3,5]

    head = createNodesList([1])
    n = 1
    print(getNormalListFromHead(solution.removeNthFromEnd(head, n))) # []

    head = createNodesList([1,2])
    n = 1
    print(getNormalListFromHead(solution.removeNthFromEnd(head, n))) # [1]

    head = createNodesList([1,2])
    n = 2
    print(getNormalListFromHead(solution.removeNthFromEnd(head, n))) # [2]
