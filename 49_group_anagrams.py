from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())
 
    
class SolutionSlow:
    def getLettersDict(self, word: str) -> dict:
        letters = {}
        if word == '':
            return {'': 1}
        for letter in word:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        return letters
    
    def groupAnagramsMy(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        
        strs_w = strs.copy()

        word_i = 0
        while word_i < len(strs_w):
            word_dict = Solution.getLettersDict(self, strs_w[word_i])
            word_anagrams = [strs_w[word_i]]

            oth_word_i = word_i + 1
            while oth_word_i < len(strs_w):
                if len(strs_w[word_i]) != len(strs_w[oth_word_i]):
                    oth_word_i += 1
                    continue
                else:
                    oth_word_dict = Solution.getLettersDict(self, strs_w[oth_word_i])
                    if len(word_dict) == 1 and '' in word_dict:
                        if len(oth_word_dict) == 1 and '' in oth_word_dict:
                            word_anagrams.append('')
                            strs_w.pop(oth_word_i)
                            continue
                    eql_flag = False
                    for letter in word_dict:
                        if letter not in oth_word_dict:
                            eql_flag = False
                            oth_word_i += 1
                            break
                        if word_dict[letter] != oth_word_dict[letter]:
                            eql_flag = False
                            oth_word_i += 1
                            break
                        else:
                            eql_flag = True
                    if eql_flag:
                        word_anagrams.append(strs_w[oth_word_i])
                        strs_w.pop(oth_word_i)
            
            word_anagrams.sort()
            if word_anagrams not in anagrams:
                anagrams.append(word_anagrams)
                strs_w.pop(word_i)
        
        return anagrams


if __name__ == '__main__':
    solution = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solution.groupAnagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]
    # assert solution.groupAnagrams(strs) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]

    strs = [""]
    print(solution.groupAnagrams(strs)) # [[""]]
    # assert solution.groupAnagrams(strs) == [[""]]

    strs = ["a"]
    print(solution.groupAnagrams(strs)) # [["a"]]
    # assert solution.groupAnagrams(strs) == [["a"]]

    strs = ["","b"]
    print(solution.groupAnagrams(strs)) # [["b"],[""]]
    # assert solution.groupAnagrams(strs) == [[''], ['b']]

    strs = ["",""]
    print(solution.groupAnagrams(strs)) # [["",""]]
    # assert solution.groupAnagrams(strs) == [["",""]]

    strs = ["ac","c"]
    print(solution.groupAnagrams(strs)) # [["c"],["ac"]]
    # assert solution.groupAnagrams(strs) == [['ac'], ['c']]
