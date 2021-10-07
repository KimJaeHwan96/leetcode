"""
[Medium] 75. Sort Colors
https://leetcode.com/problems/sort-colors/
"""
from typing import List

"""
이 문제를 보면 중요한 건 "제자리 정렬을 할 것", "직접구현 할 것" 이다.
여기서 제자리 정렬이란 엄격하게 정의하면 공간복잡도가 O(1) 로 추가되는 메모리가 없는 경우를 말하고 조금 더 넓게 정의하면 O(logN) 을 말한다.
제자리 정렬에 해당하는 정렬은 버블 정렬, 선택 정렬, 삽입 정렬, 힙 정렬, 퀵 정렬이 있다. (퀵 정렬은 넓은 의미에서의 제자리 정렬이다.)
병합 정렬은 공간복잡도가 O(N) 으로 제자리 정렬이 아니다.
출처: https://www.geeksforgeeks.org/in-place-algorithm/, https://www.geeksforgeeks.org/quick-sort/

네덜란드 국기 문제는 다익스트라(Edsger Dijkstra)기 제안한 가장 유명한 프로그래밍 문제 중 하나이다.
네덜란드 국기의 색은 빨강, 하양, 파랑 으로 이루어져있다. 문제는 각 색의 공이 무작위로 위치해있고 같은 색끼리 부어야한다는 것이다.
여기서 문제는 메모리 추가 없이 선형시간으로 정렬해야한다는 것이다. 
"""


"""
procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1

    while j <= k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
        else:
            j ← j + 1
참고:https://en.wikipedia.org/wiki/Dutch_national_flag_problem

위키피디아의 수도 코드를 보면 동작 방식을 이해할 수 있다.
i, k 를 양쪽 포인터로 두고 j 가 이동하면서 mid 값을 기준으로 스왑을 하고있다.
이를 바탕으로 코드를 작성해보았다. 
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]
            else:
                white += 1


"""
i : red  j : white  k : blue 가 된다.
white 가 움직이면 mid 값인 1 을 기준으로 스왑하고있다. 스왑한 후에는 그 위치의 값은 정렬이 됐으므로 blue 는 왼쪽, red 와 white 는 오른쪽으로 움직이고있다.  
"""

"""
위의 풀이보다 길어지고 깔끔하지는 않지만 훨씬 쉬운 방식도 있다.
0, 1, 2 만 있다고 가정하였기 때문에 각 숫자들의 수를 구하고 기존 리스트에 그 수만큼 넣어주는 것이다. 
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_cnt = 0
        one_cnt = 0
        two_cnt = 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                zero_cnt += 1

            elif nums[idx] == 1:
                one_cnt += 1

            elif nums[idx] == 2:
                two_cnt += 1

        idx = 0
        while zero_cnt > 0:
            nums[idx] = 0
            idx += 1
            zero_cnt -= 1

        while one_cnt > 0:
            nums[idx] = 1
            idx += 1
            one_cnt -= 1

        while two_cnt > 0:
            nums[idx] = 2
            idx += 1
            two_cnt -= 1


"""
똑같이 시간복잡도는 O(N) 이고 공간복잡도는 O(1) 이다.
첫번째 풀이보다는 느릴 수 있겠지만 그렇게 차니는 나지 않는다.
"""
