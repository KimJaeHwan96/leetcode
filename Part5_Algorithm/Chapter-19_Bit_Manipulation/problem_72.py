"""
[Medium] 371. Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 음수의 경우 2의 보수로 변환해주고 32비트로 만들어줌
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        # format(a & MASK, 'b').zfill(32)
        # 음수의 경우 앞자리가 1로 채워질것이도 양수면 zfill 로 0으로 채워줌
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum_num = 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum_num = carry ^ Q2
            carry = Q1 | Q3

            # 나중에 [::-1] 로 돌릴 것임
            result.append(str(sum_num))

        # 케리가 있는 경우 33비트에 둔다.
        if carry == 1:
            result.append('1')

        # https://docs.python.org/ko/3/library/functions.html#int
        # int 의 base 파라미터는 int 로 변환할 때 몇 진수로 변환할 것인지를 나타낸다.
        # 2진수로 변환 후 MASK 로 초과한 자릿수를 제거한다.
        # string 이므로 우선 2진수 양수로 변환
        result = int(''.join(result[::-1]), 2) & MASK

        # result 가 음수면 2의 보수로 변환하여 양수로 만듦
        if result > INT_MAX:
            # MASK 와 XOR 로 result 를 1 -> 0, 0 -> 1 로 1의 보수로 변환
            # 양수로 변환된 2진수(양수긴 하지만 32비트 로 제한을 하면 음수로 생각해야한다.)를 MASK 와 XOR 를 하여 32비트인 양수로 변환
            # ~ 으로 양수를 음수로 다시 변환
            result = ~(result ^ MASK)
        return result


"""
위 풀이보다 좀더 간결한 풀이 방법이 있다. 다음 풀이는 어떤 아이디어를 갖고있는지 아는 것이 중요하다.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        if a > INT_MAX:
            a = ~(a * MASK)
        return a


"""
a ^ b 는 carry 를 신경쓰지 않는 덧셈이다.
0 + 1, 1 + 0 이면 1이 되고 0 + 0 뿐만 아니라 1 + 1 도 0 이 된다.
그렇다면 carry 는 어떻게 구할까? carry 는 1 + 1 일때 발생한다. 그렇다면 AND 연산으로 구할 수 있다. 
물론 여기서 끝이 아니다. carry 가 발생하면 해당 자리수가 아니라 앞 자리수로 가기 때문에 왼쪽으로 한번 shift 해야한다.
그러면 덧셈과 carry 를 구할 수 있고 carry 가 발생하지 않을 때 까지 해당 연산을 하면 된다. (a 에는 carry 를 신경쓰지 않는 덧셈을 두고 b 에는 carry 를 둔다.)

참고: https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution
"""