from typing import Optional
from linked_list_operations import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero_node = ListNode(0, head)
        prev = zero_node
        curr = head

        while curr and curr.next:
            third = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = third
            prev.next = second

            prev = curr
            curr = third

        return zero_node.next


if __name__ == '__main__':
    solution = Solution()

    head = createNodesList([1,2,3,4])
    print(getNormalListFromHead(solution.swapPairs(head))) # [2,1,4,3]

    head = createNodesList([])
    print(getNormalListFromHead(solution.swapPairs(head))) # []

    head = createNodesList([1])
    print(getNormalListFromHead(solution.swapPairs(head))) # [1]

    head = createNodesList([1,2,3])
    print(getNormalListFromHead(solution.swapPairs(head))) # [2,1,3]
