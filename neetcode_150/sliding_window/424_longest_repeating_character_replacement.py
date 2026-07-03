from typing import Dict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: Dict[str, int] = {}
        max_length = 0

        left = 0
        most_freq = 0
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            # This is an optmisation done to avoid checking the most frequent
            # letter everytime
            most_freq = max(most_freq, counts[s[right]])

            while (right - left + 1) - most_freq > k:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
