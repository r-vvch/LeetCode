from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1

    def firstUniqCharSimple(self, s):
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for i, char in enumerate(s):
            if count[char] == 1:
                return i

        return -1


if __name__ == '__main__':
    solution = Solution()

    s = "leetcode"
    print(solution.firstUniqChar(s)) # 0

    s = "loveleetcode"
    print(solution.firstUniqChar(s)) # 2

    s = "aabb"
    print(solution.firstUniqChar(s))
