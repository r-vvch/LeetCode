from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


class SolutionMy:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right] or left == right:
            return nums[left]

        while left <= right:
            if right - left == 1:
                return min(nums[left], nums[right])

            mid = (left + right) // 2

            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                left = mid
            # Otherwise, right half is sorted
            else:
                right = mid


if __name__ == '__main__':
    solution = Solution()

    nums = [3,4,5,1,2]
    print(solution.findMin(nums)) # 1

    nums = [4,5,6,7,0,1,2]
    print(solution.findMin(nums)) # 0

    nums = [11,13,15,17]
    print(solution.findMin(nums)) # 11

    nums = [1]
    print(solution.findMin(nums)) # 1

    nums = [2,1]
    print(solution.findMin(nums)) # 1
