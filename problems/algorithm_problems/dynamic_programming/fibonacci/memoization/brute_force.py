

def fib(n: int) -> int:
    """
    Time Complexity: O(2^N)
    Space Complexity: O(n)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(6))
    print(fib(42))
