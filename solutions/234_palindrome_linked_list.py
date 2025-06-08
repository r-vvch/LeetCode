from typing import Optional
from linked_list_operations import *


class Solution:
    def isPalindromeStack(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        left = 0
        right = len(vals) - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1

        return True

    def isPalindromeFast(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Find middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the list
        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp

        # Compare nodes one by one
        first, second = head, node

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True

    isPalindrome = isPalindromeFast


if __name__ == '__main__':
    solution = Solution()

    head = createNodesList([1, 2, 2, 1])
    print(solution.isPalindrome(head)) # True

    head = createNodesList([1, 2])
    print(solution.isPalindrome(head)) # False

    head = createNodesList([1, 2, 3, 2, 1])
    print(solution.isPalindrome(head)) # True

    head = createNodesList([1, 2, 2, 1, 1, 1])
    print(solution.isPalindrome(head)) # False