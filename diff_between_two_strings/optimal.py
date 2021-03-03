

def diff_between_two_strings(source, target):
    memo = [[None for i in range(len(source) + 1)]] * (len(target) + 1)

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


if __name__ == '__main__':
    print(diff_between_two_strings("ABCDEFG", "ABDFFGH"))
