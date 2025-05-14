class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        letters = set(jewels)
        return sum(ch in letters for ch in stones)


if __name__ == '__main__':
    solution = Solution()

    jewels = "aA"
    stones = "aAAbbbb"
    print(solution.numJewelsInStones(jewels, stones)) # 3

    jewels = "z"
    stones = "ZZ"
    print(solution.numJewelsInStones(jewels, stones)) # 0
