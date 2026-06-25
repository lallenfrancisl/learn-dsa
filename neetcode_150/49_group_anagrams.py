from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map of count of letters of each word to the list of words
        # with the same count
        groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord("a")] += 1

            key = tuple(count)

            groups[key].append(word)

        return list(groups.values())
