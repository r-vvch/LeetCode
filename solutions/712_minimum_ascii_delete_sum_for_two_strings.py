class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        # dp[i][j] = maximum ASCII sum of common subsequence
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total_ascii - 2 * dp[n][m]


class SolutionOptimal:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)

        if n1 < n2:
            return self.minimumDeleteSum(s2, s1)

        dp = [[0]*(n2 + 1) for _ in range(2)]

        for i in range(n1 - 1, -1, -1):
            par = i & 1
            prev = 1 - par
            for j in range(n2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[par][j] = ord(s1[i]) + dp[prev][j+1]
                else:
                    dp[par][j] = max(dp[prev][j], dp[par][j+1])

        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total_ascii - 2*dp[0][0]


if __name__ == '__main__':
    solution = SolutionOptimal()

    s1 = "sea"
    s2 = "eat"
    print(solution.minimumDeleteSum(s1, s2)) # 231

    s1 = "delete"
    s2 = "leet"
    print(solution.minimumDeleteSum(s1, s2)) # 403
