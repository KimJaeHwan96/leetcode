"""
[medium] 148 Sort List
https://leetcode.com/problems/sort-list/
"""

"""
-문제파악
오름차순으로 정렬하는 문제다.
중요한 것은 연결리스트로 구현된 상태인것같다.

-나의 생각
병합정렬로 해결한다고 생각했을 때 연결리스트를 어떻게 나눌 수 있을까?
리스트는 쉽게 전체 길이를 구하고 분할하면 되는데 연결리스트는 어떻게 중앙을 찾아 분할 할까?
첫번째 생각: 먼저 연결리스트의 길이를 구하고 중앙을 찾기
-> 하지만 터무니 없는게 연결리스트의 길이를 구할 떄마다 O(n)의 시간이 걸리므로 어리석은 생각같다.
그렇다면 어떻게?

-책의 설명
책에서는 런너기법을 사용하면 된다고 한다.
빠른 런너와 느린 런너를 이용하는데 느린런너의 2배 빠른, 빠른 런너가 연결리스트의 끝에 가면 느린 런너는 연결리스트의 중앙에 있다고 한다.

-어떻게 문제를 해결할 것인가?
빠른 런너가 끝에 가기만 하면 느린 런너는 무조건 중앙을 가리므로 빠른 런너가 끝에 가도록 하기만 하면 된다.
이때 끝은 노드가 짝수개 일때 None, 홀수개 일때 마지막 노드를 말한다.
head ~ slow 전, slow ~ 로 리스트를 나누면 될 것 같다.
"""


# 일단 작성해본 코드
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        slow, fast, half = head, head, None
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        half = slow
        slow = slow.next
        half.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        head = ListNode()
        tmp = head
        while left.next and right.next:
            if left.val > right.val:
                tmp.next = ListNode(val=left.val)
                tmp = tmp.next
                left = left.next
            else:
                tmp.next = ListNode(val=right.val)
                tmp = tmp.next
                right = right.next

        if left:
            while left:
                tmp.next = ListNode(val=left.val)
                tmp = tmp.next
                left = left.next

        if right.next:
            while right:
                tmp.next = ListNode(val=right.val)
                tmp = tmp.next
                right = right.next

        return head.next


"""
분할하는 과정은 이해가 가지만 병합하는 과정이 난잡하며 효율도 좋아보이지 않는다.
기존 연결리스트는 두고 ListNode를 생성하며 새로운 연결리스트를 만들려는 코드다.
로직은 생각나는 대로 적은데다 에러가 나서 merge 메서드를 이해하기 쉽게 고치려 한다.
시간 복잡도, 공간 복잡도 둘다 안좋아 보인다.

left 연결리스트와 right 연결리스트의 각 노드의 값을 비교하며 next를 바꾸는 방법?

while left or right:
            if left.val < right.val:
                left, left.next = left.next, right
            else:
                right, right.next = right.next, left
-> 1->2, 3->4 를 하나의 연결리스트를 정렬할때 1이 3보다 작지만 2도 3보다 작다.
그러므로 해당 위치의 노드만 비교해야하는 것이 아니라 그 뒤의 노드도 생각해야한다.

그럼 어떻게 해야할까>
책에서는 재귀로 문제를 해결한다.

나는 하나씩 값을 비교하며 그자리에서 next를 변경하도록 하다가
참조하는 노드와 그 다음 노드까지 비교를 해야한다는 복잡한 방식으로 생각하고 있었다.
하지만 각 연결리스트의 첫번째 노드만 비교해도 각 연결리스트 중 가장 작은 값 이 뭔지 알 수 있다.
최솟값을 알고있고 그 다음 최솟값은 나중에 정하도록 재귀로 해결하면 어떨까?
순서대로 실행해야하고 값을 비교하는 즉시 비교하는 반복문보단
현재 상태에서 원하는 값을 갖고 그 값을 제외한 후 나머지 값은 다시 merge 함수를 호출하도록 하는 재귀가 좋아보인다.
"""


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        slow, fast, half = head, head, None
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        half = slow
        slow = slow.next
        half.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        if left and right:
            if left.val > right.val:
                left, right = right, left
            left.next = self.merge(left.next, right)
        return left or right
    """
    내 머릿속에는 재귀대신 반복문을 사용하려면 노드를 생성하여 연결리스트로 만들도록 해야한다고 생각된다.
    그러면 결국 처음으로 회귀하니 재귀가 가장 낫다고 생각되어진다.
    혹시 더 나은 방법이 있는지 고민해봐야겠다.
    """


# 연결리스트 -> 리스트, 리스트 -> 연결리스트로 해결
def sortList(self, head: ListNode) -> ListNode:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst.sort()
        head = ListNode()
        tmp = head
        for l in lst:
            dummy = ListNode(val=l)
            tmp.next = dummy
            tmp = dummy

        return head.next


"""
기존 구조를 이용하지 않고 새로운 노드를 이용하여 공간복잡도와 코드의 길이를 늘리고 있다.
"""
def sortList(self, head: ListNode) -> ListNode:
        lst = []
        pointer = head
        while pointer:
            lst.append(pointer.val)
            pointer = pointer.next
        lst.sort()
        pointer = head
        for l in lst:
            pointer.val = l
            pointer = pointer.next
        return head


"""
연결리스트 구조는 둔 채 포인터를 이용하여 참조하는 코드이다. 훨씬 깔끔하고 시간도 빠르다

정렬은 파이썬의 내장함수에 맞기도록 하는 방법이다. 어떻게 정렬할지 신경쓰지 않고 간결하게 작성할 수 있다.
병합정렬은 약 600ms, 각 리스트와 연결리스트로 변형하여 정렬하더라도 약 164ms 이므로 실제로는 내장함수를 이용하고
이해는 병합정렬로 이해하는 것이 도움이 될 것같다.
"""
