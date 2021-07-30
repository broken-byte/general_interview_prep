

class Solution:
    def calculate(self, s):
        """
        Time Complexity: O(N)
        Space Complexity: O(N) for stack
        """
        index = 0

        def evaluate_expression(expression):
            nonlocal index
            current_sign = 1
            current_result = 0
            while index < len(expression):
                current_character = expression[index]
                if current_character == ' ':
                    index += 1
                    continue
                elif current_character == '+':
                    current_sign = 1
                elif current_character == '-':
                    current_sign = -1
                elif current_character == '(':
                    index += 1
                    sub_expression_result: int = evaluate_expression(expression)
                    current_result += current_sign * sub_expression_result
                    current_sign = 1
                elif current_character == ')':
                    return current_result
                else:  # current_character is a digit.
                    current_number = parse_digit_entirely(expression)
                    current_result += current_number * current_sign
                    current_sign = 1
                index += 1
            return current_result

        def parse_digit_entirely(expression: str) -> int:
            nonlocal index
            digit = int(expression[index])
            while index + 1 < len(expression) and expression[index + 1].isdigit():
                digit = digit * 10 + int(expression[index + 1])
                index += 1
            return digit

        return evaluate_expression(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate(s="1+(4+5+2)-3"))
    print(solution.calculate(s="1 + 1"))
    print(solution.calculate(s=" 2-1 + 2 "))
    print(solution.calculate(s="(1+(4+5+2)-3)+(6+8)"))
