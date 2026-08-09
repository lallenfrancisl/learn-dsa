from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        p_seen = set[tuple[int, int]]()
        p_que = deque[tuple[int, int]]()

        a_seen = set[tuple[int, int]]()
        a_que = deque[tuple[int, int]]()

        for i in range(cols):
            p_que.append((0, i))
            p_seen.add((0, i))

        for i in range(1, rows):
            p_que.append((i, 0))
            p_seen.add((i, 0))

        for i in range(cols):
            a_que.append((rows - 1, i))
            a_seen.add((rows - 1, i))

        for i in range(rows - 1):
            a_que.append((i, cols - 1))
            a_seen.add((i, cols - 1))

        def bfs(que: deque[tuple[int, int]], seen: set[tuple[int, int]]) -> None:
            while que:
                i, j = que.popleft()

                for i_off, j_off in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = i + i_off, j + j_off

                    if (
                        r < rows
                        and r >= 0
                        and c < cols
                        and c >= 0
                        and heights[r][c] >= heights[i][j]
                        and (r, c) not in seen
                    ):
                        seen.add((r, c))
                        que.append((r, c))

        bfs(a_que, a_seen)
        bfs(p_que, p_seen)

        return [[coord[0], coord[1]] for coord in p_seen.intersection(a_seen)]
