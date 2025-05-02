from typing import List


class Solution:
    # O(n), O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        output = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                output.append(i)
        return output

    # O(n), O(1)
    def findDisappearedNumbersOptimal(self, nums):
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]: 
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        output = []
        for i in range(1, len(nums) + 1):
            if i != nums[i - 1]:
                output.append(i)
        return output


if __name__ == '__main__':
    solution = Solution()

    nums = [4,3,2,7,8,2,3,1]
    print(solution.findDisappearedNumbers(nums))
    # assert solution.findDisappearedNumbers(nums) == [5, 6]

    nums = [1,1]
    print(solution.findDisappearedNumbers(nums))
    # assert solution.findDisappearedNumbers(nums) == [2]
