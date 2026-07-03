class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_lookup = {}
        t_lookup = {}

        for i in range(len(s)):
            if not s_lookup.get(s[i]):
                s_lookup[s[i]] = 0

            s_lookup[s[i]] += 1

            if not t_lookup.get(t[i]):
                t_lookup[t[i]] = 0

            t_lookup[t[i]] += 1

        return s_lookup == t_lookup
