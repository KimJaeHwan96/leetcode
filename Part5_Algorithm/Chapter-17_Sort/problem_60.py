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
