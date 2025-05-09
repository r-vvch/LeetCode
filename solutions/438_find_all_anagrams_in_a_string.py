from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        output = []

        p_dict = defaultdict(int)
        for ch in p:
            p_dict[ch] += 1

        # inital pass through the [0, len(p)] window
        for i in range(len(p) - 1):
            if s[i] in p_dict:
                p_dict[s[i]] -= 1
        if len(p) - 1 < len(s) and s[len(p) - 1] in p_dict:
            p_dict[s[len(p) - 1]] -= 1
        if all(v == 0 for v in p_dict.values()):
            output.append(0)

        for i in range(len(s) - len(p) + 1):
            if s[i] in p_dict:
                p_dict[s[i]] += 1
            if i + len(p) < len(s) and s[i + len(p)] in p_dict:
                p_dict[s[i + len(p)]] -= 1

            if all(v == 0 for v in p_dict.values()):
                output.append(i + 1)

        return output


    def findAnagramsSlow(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_dict = defaultdict(int)
        for letter in p:
            p_dict[letter] += 1

        output = []
        for i in range(len(s) - len(p) + 1):
            if s[i] not in p_dict:
                continue

            p_dict_i = p_dict.copy()

            for j in range(i, min(i + len(p), len(s))):
                letter = s[j]
                if letter in p_dict_i:
                    p_dict_i[letter] -= 1
                    if p_dict_i[letter] == 0:
                        del p_dict_i[letter]
                else:
                    break

            if len(p_dict_i) == 0:
                output.append(i)

        return output


if __name__ == '__main__':
    solution = Solution()

    s = "cbaebabacd"
    p = "abc"
    print(solution.findAnagrams(s, p)) # [0,6]

    s = "abab"
    p = "ab"
    print(solution.findAnagrams(s, p)) # [0,1,2]
