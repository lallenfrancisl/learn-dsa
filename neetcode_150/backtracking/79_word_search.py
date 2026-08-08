class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path: set[tuple[int, int]] = set()

        def dfs(row: int, col: int, i: int) -> bool:
            if i == len(word):
                return True

            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or word[i] != board[row][col]
                or (row, col) in path
            ):
                return False

            path.add((row, col))
            res = (
                dfs(row + 1, col, i + 1)
                or dfs(row - 1, col, i + 1)
                or dfs(row, col + 1, i + 1)
                or dfs(row, col - 1, i + 1)
            )
            path.remove((row, col))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
