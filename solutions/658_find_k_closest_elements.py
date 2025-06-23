from bisect import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

    def findClosestElementsMy(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]

        bigger_than_x = bisect(arr, x)
        left_edge = bigger_than_x - 1 - k
        if left_edge < 0:
            left_edge = 0
        right_edge = bigger_than_x + k
        ans = arr[left_edge:right_edge]

        while len(ans) > k:
            if (abs(ans[0] - x) < abs(ans[len(ans) - 1] - x) or
                abs(ans[0] - x) == abs(ans[len(ans) - 1] - x) and ans[0] < ans[len(ans) - 1]):
                ans.pop(len(ans) - 1)
            else:
                ans.pop(0)

        return ans

    def findClosestElementsSimple(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]

        for bigger_than_x, val in enumerate(arr):
            if val > x:
                break
        ans = []
        left = bigger_than_x - 1
        right = bigger_than_x
        counter = k
        while counter > 0:
            if (left >= 0 and
                (right == len(arr) or
                 abs(arr[left] - x) < abs(arr[right] - x) or
                 abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right])):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
            counter -= 1

        ans.sort()
        return ans


if __name__ == '__main__':
    solution = Solution()

    arr = [1,2,3,4,5]
    k = 4
    x = 3
    print(solution.findClosestElements(arr, k, x)) # [1,2,3,4]

    arr = [1,1,2,3,4,5]
    k = 4
    x = -1
    print(solution.findClosestElements(arr, k, x)) # [1,1,2,3]

    arr = [1,1,2,3,4,5]
    k = 4
    x = 6
    print(solution.findClosestElements(arr, k, x)) # [2,3,4,5]

    arr = [-2,-1,1,2,3,4,5]
    k = 7
    x = 3
    print(solution.findClosestElements(arr, k, x)) # [-2,-1,1,2,3,4,5]

    arr = [1,1,1,10,10,10]
    k = 1
    x = 9
    print(solution.findClosestElements(arr, k, x)) # [10]

    arr = [1,1,2,3,3,3,4,6,8,8]
    k = 6
    x = 1
    print(solution.findClosestElements(arr, k, x))

    arr = [0,0,1,2,3,3,4,7,7,8]
    k = 3
    x = 5
    print(solution.findClosestElements(arr, k, x)) # [3,3,4]
