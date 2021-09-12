"""
[Easy] 704. Binary Search
https://leetcode.com/problems/binary-search/
"""
from bisect import bisect_left
from typing import List

"""
처음 C 언어로 이진검색을 공부할 때와 같이 코드를 작성해보았다.  
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2

            if nums[mid] > target:
                return binary_search(left, mid - 1)
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return mid

        return binary_search(0, len(nums) - 1)


"""
실행시간은 394 ms 으로 많이 느리다. 가장 처음 볼만한 풀이로 이진검색을 이해하기에 가장 좋은 방법이다.
하지만 보통 이해만 하고 실제로 사용은 안할 것이다. 파이썬 빌트인 함수로 간단하게 풀이가 가능하기 때문이다.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


"""
물론 이런 코드는 실무에서만 쓰고 코딩테스트에서 이런 풀이를 하는 것은 적절하지 않아보인다.

차라리 이진검색을 지원하는 bisect 모듈을 사용하는 것이 더 좋아보인다.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_idx = bisect_left(nums, target)

        if target_idx < len(nums) and nums[target_idx] == target:
            return target_idx
        return -1


"""
bisect 모듈은 이진 검색 그 자체를 지원한다기 보단 이진 검색을 통해 삽입을 위치를 알려준다. 그러므로 target 을 삽입할 위치를 리턴해준다.
리스트에 있는 값이 target 과 같다면 bisect_left 는 그 값의 인덱스를 리턴하고 bisect_right 는 그 값의 인덱스 + 1를 리턴한다.
그래서 bisect_left 를 사용해서 nums 에 target 의 위치를 리턴받았다. 하지만 이대로 끝난 것은 아니다.
nums 에 없는 값을 넣었을 경우에도 삽입할 인덱스를 리턴해주므로 값을 비교해주고(nums[target_idx] == target), 범위에 넘어선값이 있는지 검증한다.(target_idx < len(nums))
"""


"""
리트코드에서 bisect 모듈(241 ms)과 index 함수(385 ms)의 속도를 봤을 때 bisect 모듈이 살짝 더 빨랐다.
책에서는 bisect 모듈이 더 느리다고 하였는데 어떤상황에서 bisect 모듈 느리고 어떤상황에서 bisect 모듈 이 더 빠를지 확인해보았다.
"""

a = [i for i in range(1, 100000, 3)]

"""
정렬된 리스트를 가지고 속도 테스트를 해보았다.

timeit -n 10000 bisect.bisect_left(a,7)
443 ns ± 46.9 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

timeit -n 10000 a.index(7)
176 ns ± 12.2 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

리스트에서 앞에 있는 7을 검색했을 때 bisect 모듈보다는 index 가 더 빨랐다.

이번에는 중간쯤에 있는 77500으로 테스트 해보았다.
timeit -n 10000 bisect.bisect_left(a,77500)
486 ns ± 57 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

timeit -n 10000 a.index(77500)
238 µs ± 11 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

생각보다 속도 차이가 벌어졌다. bisect 모듈의 속도는 이전과 차이가 거의 없는 반면 index 함수는 마이크로초로 크게 늘어났다.
그렇다면 알수 있는 것은 정렬된 리스트에서 찾으려는 값이 뒤에 있을수록 bisect 모듈이 index 함수보다 빠르다는 것이다.

하지만 일반적으로 숫자가 정렬되지 않을텐데 실제 정렬되지 않는 값에서의 검색속도의 차이는 어떻게 될까?

timeit 으로 비교하기 위해 함수를 만들었다.

def binary_search(nums, target):
    nums.sort()
    target_idx = bisect.bisect_left(nums, target)
    if target_idx < len(nums) and nums[target_idx] == target:
        return target_idx
    return -1


def index_func(nums, target):
    try:
        return nums.index(target)
    except:
        return -1

리스트는 랜덤으로 생성했다.
a = [random.randrange(10000) for _ in range(2000)]

리스트의 맨 끝값을 검색할 경우의 속도이다.

timeit -n 10000 binary_search(a, 541)
23.5 µs ± 409 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

timeit -n 10000 index_func(a, 541)
1.46 µs ± 147 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

binary_search 는 정렬을 한번 한 후에 이진검색을 하므로 더 느리다.

최악의 상황으로 없는 값을 검색했을 때 속도는 비슷했다.

timeit -n 10000 binary_search(a, 9999999)
23.4 µs ± 364 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

timeit -n 10000 index_func(a, 9999999)
23.5 µs ± 291 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

극단적으로 리스트의 크기를 늘리고
a = [random.randrange(100000) for _ in range(100000)]

최악의 상황을 가정했다.

timeit -n 10000 index_func(a, 9999999)
904 µs ± 13.9 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

timeit -n 10000 binary_search(a, 9999999)
1.56 ms ± 12.4 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)


결론: 정렬이 되어있다는 가정하에 bisect 모듈이 더 빠르고 정렬이 되어있지 않으면 index 함수가 더 빠르다
"""


"""
이진 검색 알고리즘의 버그가 있다. left + right // 2  으로 인덱스를 구하는 코드이다.
수학적으로는 아무런 문제가 없지만, 컴퓨터 과학적으로 봤을 때 C 나 JAVA 의 경우 표현할 수 있는 정수값에 한계가 있다.
즉, left + right 이 연산이 오버플로우를 발생시킬 수 있다는 것이다.
사실 파이썬은 임의정밀도 정수형을 지원하여 문제가 없다고 한다.(임의정밀도는 정수를 숫자들의 배열로 표현하여 무제한 자릿수를 제공하는데 계산 속도 저하가 된다.) 
하지만 다른 프로그래밍 언어를 사용할 때 생각할 필요가 있는 문제이기도 하다.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2

            if nums[mid] > target:
                return binary_search(left, mid - 1)
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return mid

        return binary_search(0, len(nums) - 1)