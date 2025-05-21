from collections import Counter
from typing import List


class Solution:
    # better for time
    def intersectCounter(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        nums_dict_1 = Counter(nums1)

        output_arr = []
        for i in nums2:
            if nums_dict_1[i] > 0:
                output_arr.append(i)
                nums_dict_1[i] -= 1

        return output_arr

    # better for space
    def intersectSort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        output_arr = []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                output_arr.append(nums1[p1])
                p1 += 1
                p2 += 1

        return output_arr

    intersect = intersectSort


if __name__ == '__main__':
    solution = Solution()

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(solution.intersect(nums1, nums2)) # [2,2]

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    nums2_sorted = [4,4,8,9,9]
    nums1_sorted = [4,5,9]
    print(solution.intersect(nums1, nums2)) # [4,9]
