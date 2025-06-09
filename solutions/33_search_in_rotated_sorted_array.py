from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == '__main__':
    solution = Solution()

    nums = [4,5,6,7,0,1,2]
    target = 0
    print(solution.search(nums, target)) # 4

    nums = [4,5,6,7,0,1,2]
    target = 3
    print(solution.search(nums, target)) # -1

    nums = [1]
    target = 0
    print(solution.search(nums, target)) # -1
