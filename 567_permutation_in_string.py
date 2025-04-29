class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        if s1_count == s2_count:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            left += 1

            if s1_count == s2_count:
                return True

        return False

    def checkInclusionSlow(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for i in s1:
            s1_dict[i] = 1 + s1_dict.get(i, 0)

        for i in range(len(s2) - len(s1) + 1):
            s2_pos_dict = {}
            for j in range(len(s1)):
                s2_pos_dict[s2[i + j]] = 1 + s2_pos_dict.get(s2[i + j], 0)

            if s1_dict == s2_pos_dict:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()

    s1 = "ab"
    s2 = "eidbaooo"
    print(solution.checkInclusion(s1, s2)) # True

    s1 = "ab"
    s2 = "eidboaoo"
    print(solution.checkInclusion(s1, s2)) # False

    s1 = "hello"
    s2 = "ooolleoooleh"
    print(solution.checkInclusion(s1, s2)) # False

    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"
    print(solution.checkInclusion(s1, s2)) # True
