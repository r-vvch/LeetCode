from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                output[i] = nums[left] ** 2
                left += 1
            else:
                output[i] = nums[right] ** 2
                right -= 1

        return output

    def sortedSquaresMy(self, nums: List[int]) -> List[int]:
        output = []
        non_neg_i = 0
        while non_neg_i < len(nums) and nums[non_neg_i] < 0:
            non_neg_i += 1
        neg_i = non_neg_i - 1

        while non_neg_i < len(nums):
            if neg_i >= 0 and -(nums[neg_i]) < nums[non_neg_i]:
                output.append(nums[neg_i] ** 2)
                neg_i -= 1
            else:
                output.append(nums[non_neg_i] ** 2)
                non_neg_i += 1

        while neg_i >= 0:
            output.append(nums[neg_i] ** 2)
            neg_i -= 1

        return output

    def sortedSquaresCheat(self, nums: List[int]) -> List[int]:
        output = [i*i for i in nums]
        return sorted(output)


if __name__ == '__main__':
    solution = Solution()

    nums = [-4,-1,0,3,10]
    print(solution.sortedSquares(nums)) # [0,1,9,16,100]

    nums = [-7,-3,2,3,11]
    print(solution.sortedSquares(nums)) # [4,9,9,49,121]

    nums = [-1]
    print(solution.sortedSquares(nums)) # [1]
