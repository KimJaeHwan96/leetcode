"""
퀵 정렬은 피벗을 기준으로 좌우로 나눈다. 이러한 특징으로 파티션 교환 정렬이라고도 한다.
분할 방법에 따라 호어 파티션과 로무토 파티션으로 나뉜다.
"""


"""
Lomuto 파티션은 항상 맨 오른쪽의 pivot 을 택하는 단순한 방식으로 호어 파티션보다 더 간결하다.
"""


def lomuto_partition(num_list, low, high):
    pivot = num_list[high]
    left = low
    for right in range(low, high):
        if num_list[left] < pivot:
            num_list[left], num_list[right] = num_list[right], num_list[left]
            left += 1
    num_list[left], num_list[high] = num_list[high], num_list[left]
    return left


def quicksort(num_list, low, high):
    if low < high:
        pivot = lomuto_partition(num_list, low, high)
        quicksort(num_list, low, pivot - 1)
        quicksort(num_list, pivot + 1, high)


"""
Hoare 파티션은 맨 앞의 값을 pivot 으로 선택한다.
투 포인터로 맨 왼쪽 포인터와 맨 오른쪽 포인터가 있어 pivot 보다 작은 값은 왼쪽에 큰 값은 오른쪽에 둔다
"""


def hoare_partition(num_list, low, high):
    pivot = num_list[low]
    left = low
    right = high
    while True:
        while num_list[left] < pivot:
            left += 1

        while num_list[right] > pivot:
            right -= 1

        if left >= right:
            return right

        num_list[left], num_list[right] = num_list[right], num_list[left]


def quicksort(num_list, low, high):
    if low < high:
        pivot = hoare_partition(num_list, low, high)
        quicksort(num_list, low, pivot)
        quicksort(num_list, pivot + 1, high)


"""
현재 Hoare 알고리즘에서 맨 앞의 값을 pivot 으로 선택하는데 맨 뒤의 값을 pivot 으로 선택하면 RecursionError: maximum recursion depth exceeded in comparison 에러가 발생한다.

맨 뒤의 값을 pivot 으로 선택하더라도 에러가 발생하지 않으려면 아래와 같이 재귀로 호출하는 코드를 변경해야한다.

def quicksort(num_list, low, high):
    if low < high:
        pivot = hoare_partition(num_list, low, high)
        quicksort(num_list, low, pivot-1)
        quicksort(num_list, pivot, high)



         Hoare 파티션 알고리즘           VS      Lomuto 파티션 알고리즘
1.   이해하기도 어렵고 구현하기도 어렵다          이해하기 쉽고 구현하기도 쉽다.
2.   비교적 빠르다.                             Hoare 알고리즘보다 느리다.
3.    첫번째 원소을 pivot 으로 선택하지만      마지막 원소를 pivot 으로 선택한다.
    가끔 가운데 원소나 마지막 원소를 선택한다.    
4.           선형 알고리즘이고 시간 복잡도는 최악의 경우 O(N^2), 평균 O(NlogN) 으로 실행된다. 
"""
