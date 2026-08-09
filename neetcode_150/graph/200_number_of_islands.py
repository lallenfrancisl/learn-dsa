class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
