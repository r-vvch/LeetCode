from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)

    def lengthOfLISDinProg(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def lengthOfLISBrute(self, nums: List[int]) -> int:
        iss = []
        for num in nums:
            for arr in iss:
                if num > arr[-1]:
                    arr_new = arr.copy()
                    arr_new.append(num)
                    iss.append(arr_new)
            iss.append([num])

        max_len = 0
        for arr in iss:
            if len(arr) > max_len:
                max_len = len(arr)

        return max_len


if __name__ == '__main__':
    solution = Solution()

    nums = [10,9,2,5,3,7,101,18]
    print(solution.lengthOfLIS(nums)) # 4

    nums = [0,1,0,3,2,3]
    print(solution.lengthOfLIS(nums)) # 4

    nums = [7,7,7,7,7,7,7]
    print(solution.lengthOfLIS(nums)) # 1
