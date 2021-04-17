

def fib(n: int):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(len(dp)):
        tabulate(dp, i)
    return dp[-1]


def tabulate(dp: list, i: int):
    if i + 2 < len(dp):
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
    elif i + 1 < len(dp):
        dp[i + 1] += dp[i]


if __name__ == '__main__':
    print(fib(6))
    print(fib(42))
    print(fib(3000))
