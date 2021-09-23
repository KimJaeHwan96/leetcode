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
