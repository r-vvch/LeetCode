from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0:1}
        total = 0
        count = 0
        for n in nums:
            total += n
            if total - k in sub_num:
                count += sub_num[total-k]
            sub_num[total] = 1 + sub_num.get(total, 0)
        return count

    def subarraySumNaive(self, nums: List[int], k: int) -> int:
        p1 = 0
        p2 = 0
        output = 0
        while p1 < len(nums):
            p2 = p1 + 1
            while p2 < len(nums) + 1:
                if sum(nums[p1:p2]) == k:
                    while sum(nums[p1:p2]) == k and p2 < len(nums) + 1:
                        output += 1
                        p2 += 1
                    break
                p2 += 1
            p1 += 1    
        return output


if __name__ == '__main__':
    solution = Solution()

    nums = [1,1,1]
    k = 2
    print(solution.subarraySum(nums, k)) # 2
    # assert solution.subarraySum(nums, k) == 2

    nums = [1,2,3]
    k = 3
    print(solution.subarraySum(nums, k)) # 2
    # assert solution.subarraySum(nums, k) == 2

    nums = [1]
    k = 0
    print(solution.subarraySum(nums, k)) # 0
    # assert solution.subarraySum(nums, k) == 0

    nums = [1,-1,0]
    k = 0
    print(solution.subarraySum(nums, k)) # 3
    # assert solution.subarraySum(nums, k) == 3
