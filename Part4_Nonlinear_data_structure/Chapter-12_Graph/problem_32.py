"""
[medium] 200. Number of Islands
https://leetcode.com/problems/number-of-islands/
"""
from typing import List


"""
각 내부 리스트를 순회하면서 '1' 을 발견하여 섬의 개수를 찾는 문제이다.
'1'을 발견했다면 발견한 위치에서 동서남북 으로 이동하며 '1' 이 있는지 찾는 것으로 풀이가 가능해보인다.  
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check_island(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return False

            grid[row][col] = '0'

            check_island(row, col + 1)
            check_island(row, col - 1)
            check_island(row + 1, col)
            check_island(row - 1, col)

        Island_num = 0
        for row_idx, row in enumerate(grid):
            for col_idx in range(len(row)):
                if grid[row_idx][col_idx] == '1':
                    breakpoint()
                    check_island(row_idx, col_idx)
                    Island_num += 1
        return Island_num


"""
곰곰히 생각해보면 그래프의 형태는 아니지만 동서남북으로 연결된 그래프로 생각할 수도 있어보인다.
섬을 찾을 때 

check_island(row, col + 1)
check_island(row, col - 1)
check_island(row + 1, col)
check_island(row - 1, col)

로 풀이하였지만

check_island(row + 1, col)
check_island(row - 1, col)
check_island(row, col + 1)
check_island(row, col - 1)
의 순서로 두면 DFS 로 보인다.
"""
