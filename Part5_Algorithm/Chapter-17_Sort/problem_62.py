"""
[Easy] 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""
import collections

"""
단순히 두 문자열을 비교하는 문제이므로 간단하다. 정렬해서 비교만 하면 된다.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


""" 
위 풀이가 간결하고 쉽지만 sorted 내장 함수는 정렬 후 새로운 문자열을 리턴하므로 공간복잡도가 O(N) 이 된다.
다른 사람들의 풀이를 보다가 재밌는 풀이를 봤다. 더 빠르고 메모리도 덜 사용하는 풀이이다.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.defaultdict(int)
        for x in s:
            tracker[x] += 1

        for x in t:
            tracker[x] -= 1
        return all(x == 0 for x in tracker.values())


"""
반복문 3번을 실행하니 시간복잡도는 O(N) 이다.
정렬된 문자열을 리턴을 하는 것이 아니고 하나의 defaultdict 를 사용하므로 s 와 t 의 정렬된 문자열을 리턴하는 첫 번째 풀이보다 메모리를 덜 사용한다. 
"""