from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


def createLinkedList(arr) -> list[ListNode]:
    if arr == []:
        return []
    output_reversed = [ListNode(arr[-1], None)]
    for i in range(len(arr) - 2, -1, -1):
        output_reversed.append(ListNode(arr[i], output_reversed[-1]))
    return list(reversed(output_reversed))


def getNormalListFromHead(head) -> list[int]:
    output = []
    curr = head
    if curr is None:
        return []
    while curr.next is not None:
        output.append(curr.val)
        curr = curr.next
    output.append(curr.val)
    return output


if __name__ == '__main__':
    solution = Solution()

    arr = [1, 2, 3, 4, 5]
    arr = createLinkedList(arr)
    head = arr[0]
    output = getNormalListFromHead(solution.reverseList(head))
    print(output)
    assert output == [5, 4, 3, 2, 1]

    arr = [1, 2]
    arr = createLinkedList(arr)
    head = arr[0]
    output = getNormalListFromHead(solution.reverseList(head))
    print(output)
    assert output == [2, 1]

    arr = []
    arr = createLinkedList(arr)
    head = None
    output = getNormalListFromHead(solution.reverseList(head))
    print(output)
    assert output == []
