from enum import Enum


class Sign(Enum):
    POSITIVE, NEGATIVE = 1, -1


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        previous_operand = 0
        result = 0
        sign = Sign.POSITIVE
        for current_character in s:
            if current_character.isdigit():
                previous_operand = (previous_operand * 10) + int(current_character)
            elif current_character == '+':
                result += sign.value * previous_operand
                sign = Sign.POSITIVE
                previous_operand = 0
            elif current_character == '-':
                result += sign.value * previous_operand
                sign = Sign.NEGATIVE
                previous_operand = 0
            elif current_character == '(':
                stack.append(result)
                stack.append(sign)
                sign = Sign.POSITIVE
                result = 0
            elif current_character == ')':
                result += sign.value * previous_operand
                sign_of_total_sub_expression: Sign = stack.pop()
                result *= sign_of_total_sub_expression.value
                result_before_sub_expression: int = stack.pop()
                result += result_before_sub_expression
                previous_operand = 0
        return result + sign.value * previous_operand


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate(s="1 + 1"))
    print(solution.calculate(s=" 2-1 + 2 "))
    print(solution.calculate(s="(1+(4+5+2)-3)+(6+8)"))
