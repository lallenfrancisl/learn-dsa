class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        l_ptr = 0
        r_ptr = len(cleaned) - 1

        while l_ptr < len(cleaned):
            if cleaned[l_ptr] != cleaned[r_ptr]:
                return False

            l_ptr += 1
            r_ptr -= 1

        return True
