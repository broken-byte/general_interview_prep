

def fib(n: int) -> int:
    """
    Time Complexity: O(2*N) -> O(N)
    Space Complexity: O(n)
    """
    memo: dict = {}

    def fib_recursively(f: int) -> int:
        if f in memo:
            return memo[f]
        elif f == 0:
            return 0
        elif f == 1:
            return 1
        memo[f] = fib_recursively(f - 1) + fib_recursively(f - 2)
        return memo[f]

    return fib_recursively(n)


if __name__ == '__main__':
    print(fib(6))
    print(fib(42))
