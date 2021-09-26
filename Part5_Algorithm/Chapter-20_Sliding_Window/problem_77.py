"""
[Medium] 424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/
"""
from collections import Counter

"""
어떻게 풀이할지 고민해봤을 때 그전 풀이와 동일하게 투 포인터로 윈도우 크기를 늘리고 가장 빈도수가 많은 값은 Counter 로 풀이하면 되지 않을까 생각이 든다.
"""


class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        left = 0
        counts = Counter()
        for right in range(1, len(string) + 1):
            counts[string[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]
            # k 초과시 왼쪽 포인터 이동
            # 이 때  right - left - max_char_n > k 로 조건문을 둔 이유는 무엇일까?
            # 해당 조건문이 True 이면 "k 번만큼 변경한 가장 긴 길이 + 1" 이다.
            if right - left - max_char_n > k:
                counts[string[left]] -= 1
                left += 1
        return right - left


"""
string 이 'AACBD' 이고 k 가 2일때 가장 긴 길이는 AACB 이다.
하지만 위의 로직으로 디버깅 할 때 right - left 를 하면 5 - 1 로 'ACBD' 이 된다. 물론 가장 긴 길이 + 1 일때마다 left 를 옮기니 결국 같은 답이다.
하지만 답은 구하되 언뜻 보기에 이해가 안되므로 좀더 직관적이고 로직을 따라가볼 떄 이해가 되도록 개선해봤다.
"""


class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        left = 0
        max_length = 0
        counts = Counter()
        for right in range(1, len(string) + 1):
            counts[string[right - 1]] += 1
            max_char_n = counts.most_common(1)[0][1]

            # right - left - max_char_n == k 의 의미는 k 번만큼 변경한 가장 긴 길이 일때 이다.
            if right - left - max_char_n == k:
                # right - left if max_length < right - left else max_length 을 하지 않는 이유
                # 윈도우 크기가 커지므로 갱신이 이뤄지면 그전 max_length 보다 클 수밖에 없음
                max_length = right - left
            # 윈도우 크기가 더 커지면 left 포인터를 옮긴다.
            elif right - left - max_char_n > k:
                counts[string[left]] -= 1
                left += 1

        # ex) string 이 "AAAA" 이고 k 가 2라고 했을 때 max_length 가 반복문 내에서 갱신되지 않음
        # 이런 경우 문자열 길이 만큼 리턴
        if max_length == 0:
            max_length = right - left

        return max_length


"""
윈도우 크기를 늘리면서 가장 긴 문자열이 될 때마다 갱신을 하고 윈도우의 크기가 커지면 left 포인터를 옮기며 줄여준다.
윈도우의 크기가 작을 때는 right 가 늘려주니 신경쓸 필요는 없다.
그리고 첫 번째 코드와 달리 변경할 필요가 없는 문자열일 경우에 대한 예외처리가 있어야한다.

간결하기는 첫번째 코드가 더 낫다. 게다가 첫 번째 풀이보다 두번째 풀이가 지저분해보인다. 하지만 두번째 코드가 난잡해 보일수는 있지만 좀더 명확해 보인다.
나중에 다시 보면서 어떤 코드가 더 직관적이고 읽기 쉬운지 비교해 볼 것이다.
지금은 두 번째 로직이 더 낫지 않을까 하는 생각이 든다.
"""
