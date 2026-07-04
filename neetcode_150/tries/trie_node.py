from typing import Dict


class TrieNode:
    children: Dict[str, "TrieNode"]
    is_end: bool

    def __init__(self) -> None:
        self.children = {}
        self.is_end = False
