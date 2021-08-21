"""
[Medium] 621. Task Scheduler
https://leetcode.com/problems/task-scheduler/
"""
from collections import Counter

"""
problem 79 를 해결한 방법과 동일하게 우선순위 큐를 해결하기에는 task 의 개수를 계속 업데이트해야하는 문제가 있다.
그러므로 다른 방법이 없을까 고민하다 책에서 Counter 를 사용하는 힌트를 얻었다.
파이썬 공식문서 collections 모듈을 보면서 해당 문제를 해결하는 알고리즘에 대해서 고민을 했다.  
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        tasks_counter = Counter(tasks)
        while tasks_counter:
            # n + 1 개의 task 추출
            tasks_common = tasks_counter.most_common(n + 1)
            c = Counter()
            for task in tasks_common:
                c[task[0]] = 1

            if len(tasks_common) < n + 1:
                # idle 이 발생하는 상황에는 idle 도 포함
                result += n + 1
            else:
                # idle 이 필요없으면 제외
                result += len(tasks_common)

            # task 업데이트(추출한 task 업데이트)
            tasks_counter.subtract(c)

            # 책에서 알려준 0인 task 제거하는 방법...
            tasks_counter += Counter()

        if len(tasks_common) < n + 1:
            # 마지막 task 이후 idle 도 계산한 경우 제외하는 코드
            result -= ((n + 1) - len(tasks_common))

        return result


"""
문제는 해결했지만 실행시간이 700 ms 이 걸렸다. 최적화가 덜 되어있다. 
가장 먼저 눈에 리팩토링 하고싶은 부분은 마지막 task 이고 idle 이 포함된 경우 다시 빼줘야하는 것이다.
그리고 while 과 for 의 중첩 반복문이 보인다. 

최적화가 필요한 로직은 다음과 같다.
1. 마지막 task 추출이 언제인지 판단할 필요없이 반복문 하나로 계산하기
2. 이중 반복문 개선하기
"""


"""
책에서 본 풀이는 다음과 같다.
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0
        while True:
            sub_count = 0

            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += Counter()

            if not counter:
                break

            result += n - sub_count + 1
        return result


"""
내가 작성한 코드와 다른 점은 while 문을 쓸 때 무한루프를 사용하고 idle 을 계산하기전에 마지막 task 추출인 경우 break 를 사용하는 경우이다.
다만 실무에서는 무한루프 자체가 너무 위험하다고 생각되어 문제풀이에서만 사용하는 것이 좋다고 생각되어진다.
그리고 Counter 에 추출한 task 를 제거할때 task(key) 만 입력해주면 - 1이 된다는 점이다. 
Counter 는 강력한 도구이지만 성능상 빠른 편은 아닌 것 같다. 
"""
