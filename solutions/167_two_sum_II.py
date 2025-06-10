from typing import List


class Solution:
    # O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1

    # O(nlogn)
    def twoSumSlow(self, numbers: List[int], target: int) -> List[int]:
        for left in range(len(numbers)):
            right_min = left + 1
            right_max = len(numbers) - 1
            while right_min <= right_max < len(numbers):
                right = (right_max + right_min) // 2
                if numbers[left] + numbers[right] == target:
                    return [left + 1, right + 1]
                elif (right_max - right_min == 1 and right + 1 < len(numbers)
                        and numbers[left] + numbers[right + 1] == target):
                    return [left + 1, right + 2]
                elif right_min == right == right_max:
                    break
                elif numbers[left] + numbers[right] < target:
                    right_min = right + 1
                else:
                    right_max = right - 1


if __name__ == '__main__':
    solution = Solution()

    numbers = [2,7,11,15]
    target = 9
    print(solution.twoSum(numbers, target)) # [1,2]

    numbers = [2,3,4]
    target = 6
    print(solution.twoSum(numbers, target)) # [1,3]

    numbers = [-1,0]
    target = -1
    print(solution.twoSum(numbers, target)) # [1,2]

    numbers = [5,25,75]
    target = 100
    print(solution.twoSum(numbers, target)) # [2,3]

    numbers = [3,24,50,79,88,150,345]
    target = 200
    print(solution.twoSum(numbers, target)) # [3,6]

    numbers = [1,3,4,4]
    target = 8
    print(solution.twoSum(numbers, target)) # [3,4]

    numbers = [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,
               227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,
               394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,
               650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,
               863,874,887,896,916,920,926,927,930,933,957,981,997]
    target = 542
    print(solution.twoSum(numbers, target)) # [3,4]
