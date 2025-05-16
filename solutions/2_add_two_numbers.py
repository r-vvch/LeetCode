from typing import Optional


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
    def getNumFromLinkedList(self, ll: ListNode) -> int:
        num = 0
        ll_len_counter = 0
        list_node = ll
        while list_node:
            num += 10 ** ll_len_counter * list_node.val
            ll_len_counter += 1
            list_node = list_node.next
        return num

    def getLinkedListFromNum(self, num: int) -> ListNode:
        num_str = str(num)
        curr_list_node = ListNode(int(num_str[0]), None)
        for i in range(1, len(num_str)):
            curr_list_node = ListNode(int(num_str[i]), curr_list_node)
        return curr_list_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getNumFromLinkedList(l1)
        num2 = self.getNumFromLinkedList(l2)
        ll_out = self.getLinkedListFromNum(num1 + num2)
        return ll_out


class SolutionFast:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_node_0 = ListNode(0)
        tail = list_node_0
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = list_node_0.next
        list_node_0.next = None
        return result


if __name__ == '__main__':
    solution = Solution()

    l1 = createNodesList([2,4,3])
    l2 = createNodesList([5,6,4])
    # print(solution.getNumFromLinkedList(l1))
    # print(solution.getNumFromLinkedList(l2))
    print(getNormalListFromHead(solution.addTwoNumbers(l1, l2))) # [7,0,8]

    l1 = createNodesList([0])
    l2 = createNodesList([0])
    print(getNormalListFromHead(solution.addTwoNumbers(l1, l2))) # [0]

    l1 = createNodesList([9,9,9,9,9,9,9])
    l2 = createNodesList([9,9,9,9])
    print(getNormalListFromHead(solution.addTwoNumbers(l1, l2))) # [8,9,9,9,0,0,0,1]
