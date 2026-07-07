from tries.trie_node import TrieNode


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.is_end = True

    def search(self, word: str) -> bool:
        return self._search_word(0, self.root, word)

    def _search_word(self, j: int, root: TrieNode, word: str) -> bool:
        cur = root
        for i in range(j, len(word)):
            c = word[i]

            if c == ".":
                for child in cur.children.values():
                    if self._search_word(i + 1, child, word):
                        return True

                return False
            else:
                if c not in cur.children:
                    return False

                cur = cur.children[c]

        return cur.is_end
