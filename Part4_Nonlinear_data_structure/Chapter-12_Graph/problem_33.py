"""
[medium] 17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List

"""
가능한 모든 문자의 경우의 수를 구하는 문제이다. 
우선 가장 단순하게 브루트 포스를 이용하여 풀 생각을 했는데 어려워 보였다.
예를 들어 이터러블한 객체가 2개 또는 3개 있을때 이중 반복문, 삼중 반복문으로 완전탐색이 가능하지만 이 문제는 숫자에 대응하는 문자가 있기 때문에 오히러 더 어렵게 보여진다. 

하나의 완전한 문자를 만들려면 재귀로 DFS 를 구현하면 되지 않을까 생각이 들었다.
각 숫자에 해당하는 문자가 연결되어있는 그래프라고 생각 하는 것이다.
"23" 으로 입력되었다고 가정하면 2('a', 'b', 'c') 와 3('d', 'e', 'f') 이고 a 는 def 와 b 도 def 와 c 도 def 와 연경되었다고 생각하는 것이다.
a, b, c는 연결되지 않았고 같은 부모 노드를 가진다고 가정한다.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def phone_number_dfs(digits_idx, alphabet):
            if len(digits) == len(alphabet):
                alphabet_path.append(alphabet)
                return

            for idx in range(digits_idx, len(digits)):
                for letter in graph[digits[idx]]:
                    phone_number_dfs(idx + 1, alphabet + letter)

        if not digits:
            return []

        graph = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        alphabet_path = []
        phone_number_dfs(0, '')

        return alphabet_path


"""
문제 풀이를 다음과 같이 정리했다.

1. digits 순회
2. 순회한 digits 의 값들을 dictionary 에 넣어서 문자열을 가져옴
3. 가져온 문자열 순회
4. 해당 과정을 재귀로 DFS 함


하지만 다음과 같은 난관에 봉착했다.
"입력된 전화번호의 조합을 구하는 것도 재귀로 구해야하는데 그 조합을 리스트에 넣는 것도 재귀로 구해야한다."
그렇기 때문에 단순하게 DFS 를 적용하면 안된다. 

풀이 순서에 하나를 추가해야한다.

1. digits 순회
2. 순회한 digits 의 값들을 dictionary 에 넣어서 문자열을 가져옴
3. 가져온 문자열 순회
★ 4. 문자열의 조합이 완성되면 (len(digits) == len(alphabet)) 리스트에 넣는다.
5. 해당 과정을 재귀로 DFS 함

어떻게 문자열의 조합을 완성할까? 처음든 생각은 다른 재귀와 같이 문자열 혹은 리스트에 넣어 기억하는 방법이 있지만 좀더 깔끔하게 "인자" 로 기억하는 방법이 있다.
즉 phone_number_dfs(idx + 1, alphabet + letter) 다음과 같이 구현하는 것이다.
"""
