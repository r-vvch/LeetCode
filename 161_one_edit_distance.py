class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # for convenience we will say that s is the longer str
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        # now we know that s is the longer one:
        if len(s) > len(t) + 1:
            return False
        for i in range(len(t)):
            if t[i] != s[i]:
                if len(s) == len(t):
                    # if the remainders are equal - we can do with one edit, if not - not
                    return s[i + 1:] == t[i + 1:]
                else:
                    # if the remainders with one deletion are equal - True, not - False
                    return s[i + 1:] == t[i:]
        return len(s) == len(t) + 1


if __name__ == '__main__':
    solution = Solution()

    s = "ab"
    t = "acb"
    print(solution.isOneEditDistance(s, t)) # True
    assert solution.isOneEditDistance(s, t) == True

    s = ""
    t = ""
    print(solution.isOneEditDistance(s, t)) # False
    assert solution.isOneEditDistance(s, t) == False
