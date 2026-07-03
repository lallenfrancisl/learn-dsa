class Solution:
    def do(self, words: list[str]) -> list[str]:
        return self.decode(self.encode(words))

    def encode(self, strs: list[str]) -> str:
        # write the header
        encoded = ""
        for word in strs:
            encoded += f"{len(word)},"

        encoded += "#"

        # write the body
        for word in strs:
            encoded += word

        return encoded

    def decode(self, s: str) -> list[str]:
        i: int = 0

        # parse the header
        sizes: list[int] = []
        buffer: str = ""
        while i < len(s) and s[i] != "#":
            if s[i] == ",":
                sizes.append(int(buffer, base=10))
                buffer = ""
            else:
                buffer += s[i]

            i += 1

        # parse the body
        words: list[str] = []
        for size in sizes:
            word = ""
            for j in range(i + 1, i + 1 + size):
                word += s[j]

            words.append(word)
            i = i + size

        return words
