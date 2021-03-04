

def diff_between_two_strings(source, target):
    '''
    First Solution
    ---------------------------------
    n, m = len(source), len(target)
    memo = [[0] * m] * n

    def dp(i, j):
        if i == len(source) or j == len(target):  # If we've iterated through all of one of the strings
            return len(target) - j
        elif memo[i][j] is None:
            if source[i] == target[j]:
                memo[i][j] = dp(i + 1, j + 1)
            else:
                memo[i][j] = 1 + min(
                    dp(i + 1, j),  # Subtract from source (-)
                    dp(i, j + 1)   # Add to Source (+)
                )
        return memo[i][j]

    i, j = 0, 0
    ans = []
    while i < len(source) and j < len(target):
        if source[i] == target[j]:
            ans.append(source[i])
            i += 1
            j += 1
        else:
            if dp(i + 1, j) <= dp(i, j + 1):
                ans.append('-' + source[i])
                i += 1
            else:
                ans.append('+' + target[j])
                j += 1
    while j < len(target):  # If we haven't iterated through all of target yet, we know the answer already
        ans.append('+' + target[j])
        j += 1
    return ans
    Second Solution
    '''
    n, m = len(source), len(target)
    dp = memo = [[0] * (m + 1)] * (n + 1)
    ans = []
    for i in range(n):
        dp[i][m] = 0
    for j in range(m):
        dp[n][j] = m - j
    for i in range(n - 1, 0):
        for j in range(m - 1, 0):
            if source[i] == target[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i + 1][j],  # Subtract from source (-)
                    dp[i][j + 1]   # Add to source (+)
                )
    return dp[0][0]


if __name__ == '__main__':
    test = diff_between_two_strings("ABCDEFG", "ABDFFGH")
    print(test)
    assert(test == ["A","B","-C","D","-E","F","+F","G","+H"])
