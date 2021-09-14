"""
[Hard] 76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
"""
from collections import Counter

"""
문제를 보자마자 숨이 턱 막혔다. 어떻게 풀이하는 지 감이 안왔기 때문이다.
생각을 정리하면서 한가지 해결해야하는 문제가 있다는 것을 깨달았다.
"어떻게 윈도우 사이즈를 줄일 것인가?"
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 오른쪽 포인터를 늘이면서 윈도우 크기 늘림
        need_char = Counter(t)
        total_need_char = len(t)

        # left 는 왼쪽 포인터, start 와 end 는 t의 문자들이 포함된 최소 윈도우를 저장하기 위한 투 포인터
        left = start = end = 0
        for right, char in enumerate(s, 1):
            total_need_char -= need_char[char] > 0
            need_char[char] -= 1

            # 필요한 값들이 전부 포함되면
            if total_need_char == 0:

                # 왼쪽 포인터가 필요없는 문자를 가리키면 오른쪽으로 이동한다.
                while left < right and need_char[s[left]] < 0:
                    need_char[s[left]] += 1
                    left += 1

                # 윈도우를 start, end 에 저장
                if not end or right - left <= end - start:
                    start, end = left, right

                # left 포인터 에서 시작하는 최소 윈도우 는 이미 start, end 에 저장함.
                # 현재 left 포인터에서의 최소 윈도우는 구했으므로 left 를 오른쪽으로 이동
                need_char[s[left]] += 1
                left += 1
                total_need_char += 1

        return s[start: end]


"""
책의 풀이를 보면서 하나씩 정리해 보았다.

1. 오른쪽 포인터를 늘인다.
2. 필요한 값들이 전부 포함되면(total_need_char == 0 이면) 최소 윈도우 크기를 갱신한다.
3. 윈도우를 갱신하기 전에 왼쪽 포인터가 필요없는 값이면 오른쪽으로 이동한다.
4. 현재 가리키고 있는 왼쪽 포인터에서의 최소 윈도우 크기를 구했으므로 왼쪽 포인터를 오른쪽으로 이동한다. (이동하면서 각 값들을 갱신한다.)

start 와 end 를 0 으로 초기화한 이유는 찾으려는 값이 없는 경우 "" 으로 빈값을 리턴해주기 위함이다.
"""
