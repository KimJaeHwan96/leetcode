"""
[Medium] 240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
import bisect
from typing import List

"""
행렬 M X N 에서 target 을 찾기위한 풀이방법으로 브루트 포스를 생각해봤다.
시간복잡도는 O(M * N) 으로 매우 느린 속도로 보인다. M 과 N 이 최대 300으로 같다면 최악의 경우 O(N^2) 으로도 볼 수 있다.
그러므로 브루트 포스보단 각 행(리스트)를 가져와 이진검색을 하는 것이 차라리 더 낫아 보인다. 그러면 시간복잡도는 O(M * logN) 으로 브루트 포스보단 월씬 빨라 보인다.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for num_list in matrix:
            target_idx = bisect.bisect_left(num_list, target)
            # target 이 리스트 내의 값중 가장 큰 값이면 맨 뒤에 둔다. 리스트는 [1,4,5,10,15] 이고 target 이 20 인 경우 5를 리턴
            if len(num_list) > target_idx and num_list[target_idx] == target:
                return True
        return False


"""
이진 검색으로 풀이하는 방법 말고 파이썬스러운 풀이방법이 있다.
각 리스트를 조회하며 target 이 있는지 여부를 in 으로 찾아 리스트로 만든다.
그리고 any 로 있는지 없는지 찾는다.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any([target in num_list for num_list in matrix])


"""
이런 풀이방식도 있다. 2차원 리스트 전체를 보며 target 을 찾는 것이다.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            current_value = matrix[row][col]
            if target < current_value:
                col -= 1
            elif target > current_value:
                row += 1
            else:
                return True
        return False


"""
첫 행의 맨 뒤의 값을 기준으로 아래에 있는 값은 더 큰 값들만 있고 왼쪽에 있는 값은 더 작은 값들만 있다.
row = 0
col = len(matrix[0]) - 1
으로 matrix[row][col] 이 값을 기준으로 값들을 찾는다.
만약 target 이 matrix[row][col] 보다 크면 0번째 리스트는 전부 제외할 수 있고 matrix[row][col] 보다 작으면 len(matrix[0]) - 1 열은 더이상 관심을 둘 필요가 없다.
(왜냐하면 target 이 matrix[row][col] 보다 더 작으면 len(matrix[0]) - 1 열의 값들보단 작을 수 밖에 없고 matrix[row][col] 보다 크면 0번째 행의 값들보단 클 수 밖에 없다.)
그래서 왼쪽과 아래쪽으로만 가면서 target 을 찾으면 된다.
"""