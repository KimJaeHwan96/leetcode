"""
[medium] 147. Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/
"""
from typing import Optional


"""
연결리스트를 삽입정렬하는 문제로 삽입정렬에 대한 이해가 필요하다.

삽입정렬이란 앞에서 부터 정렬된 부분과 비교하여 자신의 위치를 찾아 삽입하는 것이다.
삽입정렬의 핵심은 정렬된 부분과 정렬되지 않는 부분으로 나뉘는 것이다.

연결리스트도 이와 마찬가지로 정렬된 연결리스트와 정렬되지 않는 연결리스트로 나누어서 정렬을 하면된다. 
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = parent = ListNode()
        while head:
            while current.next and current.next.val < head.val:
                current = current.next

            current.next, head.next, head = head, current.next, head.next
            current = parent

        return parent.next


"""
여기서는 parent 가 정렬된 연결리스트를 가리키고 head 는 정렬되지 않은 연결리스트를 가리킨다.
current 는 위치를 찾는 포인터가 된다.

current 는 head 의 값이 current 보다 크지만 current.next 보단 작은 위치에 삽입된다.
"""


"""
너무 느리게 실행되어 최적화가 가능한 부분을 찾아보았다.
current = parent 는 current 가 항상 맨앞으로 가게되는데 위에서 말한대로 "current 는 head 의 값이 current 보다 크지만 current.next 보단 작은 위치에 삽입된다."
그러므로 head 의 값이 current 의 값보다 큰 경우 굳이 맨앞으로 이동할 필요가 없다. 

그러면 다음과 같이 코드를 작성하면 된다.
current = parent       ======>   if head and current.val > head.val:
                                    current = parent
"""


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = parent = ListNode()
        while head:
            while current.next and current.next.val < head.val:
                current = current.next

            current.next, head.next, head = head, current.next, head.next
            if head and current.val > head.val:
                current = parent

        return parent.next


"""
첫번째 풀이에서 조건문 추가하여 current 포인터를 맨앞으로 가야할 때만 옮기게만 하였는데 실행시간이 크게 줗었다.
1932 ms -> 168 ms 으로 싱행시간이 약 10분의 1이 줄어들었다.
"""
