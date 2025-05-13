from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        curr = m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[curr] = nums1[p1]
                p1 -= 1
            else:
                nums1[curr] = nums2[p2]
                p2 -= 1
            curr -= 1

    def merge_sort(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()


if __name__ == '__main__':
    solution = Solution()
    
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1) # [1,2,2,3,5,6]

    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1) # [1,2,3,4,5,6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(nums1) # [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(nums1) # [1]
