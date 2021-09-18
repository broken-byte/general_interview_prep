

class Solution:
    """
    N = len(num)
    Time Complexity: O(4^N*N)
    Space Complexity: O(N)
    """
    def addOperators(self, num: 'str', target: 'int') -> 'list[str]':

        n: int = len(num)
        answers: list[str] = []

        def recurse(index: int, prev_operand: int, current_operand: int, value: int, string: list[str]):

            # Done processing all the digits in num
            if index == n:
                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand: int = current_operand * 10 + int(num[index])
            str_operand = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:
                # NO OP recursion
                recurse(
                    index + 1,
                    prev_operand,
                    current_operand,
                    value,
                    string
                )

            # ADDITION
            string.append('+')
            string.append(str_operand)
            recurse(
                index + 1,
                prev_operand=current_operand,
                current_operand=0,
                value=value + current_operand,
                string=string
            )
            string.pop()
            string.pop()

            # Can subtract or multiply only if there are some previous operands
            if len(string) != 0:
                # SUBTRACTION
                string.append('-')
                string.append(str_operand)
                recurse(
                    index + 1,
                    prev_operand=-current_operand,
                    current_operand=0,
                    value=value - current_operand,
                    string=string
                )
                string.pop()
                string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_operand)
                recurse(
                    index + 1,
                    prev_operand=current_operand * prev_operand,
                    current_operand=0,
                    value=value - prev_operand + (current_operand * prev_operand),
                    string=string
                )
                string.pop()
                string.pop()

        recurse(0, 0, 0, 0, [])
        return answers


if __name__ == '__main__':
    solution = Solution()
    print(solution.addOperators(num="123", target=6))
    print(solution.addOperators(num="232", target=8))
    print(solution.addOperators(num="105", target=5))
    print(solution.addOperators(num="00", target=0))
    print(solution.addOperators(num="3456237490", target=9191))
