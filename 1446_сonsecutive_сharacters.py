class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 0
        last_char = s[0]
        i = 1
        curr_power = 1
        while i < len(s):
            if s[i] == last_char:
                curr_power += 1
            else:
                if curr_power > max_power:
                    max_power = curr_power
                curr_power = 1
                last_char = s[i]
            i += 1

        return max(curr_power, max_power)


if __name__ == '__main__':
    solution = Solution()

    s = "leetcode"
    print(solution.maxPower(s)) # 2

    s = "abbcccddddeeeeedcba"
    print(solution.maxPower(s)) # 5

    s = "cc"
    print(solution.maxPower(s)) # 2

    s = 'c'
    print(solution.maxPower(s)) # 2
