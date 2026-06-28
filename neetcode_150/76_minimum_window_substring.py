from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        want = len(t)
        lookup: Dict[str, int] = {}
        for i in t:
            lookup[i] = 1 + lookup.get(i, 0)

        have = 0
        counts: Dict[str, int] = {}
        window = (-1, -1)

        left = 0
        right = 0
        for right in range(len(s)):
            c = s[right]
            if c in lookup:
                counts[c] = 1 + counts.get(c, 0)

                if counts[c] <= lookup[c]:
                    have += 1

            while have == want:
                cur_length = right - left + 1
                window_length = window[1] - window[0] + 1

                if cur_length <= window_length or window[0] < 0:
                    window = (left, right)

                if s[left] in counts:
                    counts[s[left]] -= 1

                    if counts[s[left]] < lookup[s[left]]:
                        have -= 1

                left += 1

        if window[0] >= 0:
            return s[window[0] : window[1] + 1]

        return ""
