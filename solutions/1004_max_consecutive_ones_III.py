from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, zeros, ans = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    solution = Solution()

    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(solution.longestOnes(nums, k)) # 6

    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(solution.longestOnes(nums, k)) # 10

    nums = [0,0,0,0]
    k = 0
    print(solution.longestOnes(nums, k)) # 0
