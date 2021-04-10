from collections import Counter


class Solution:
    def __init__(self):
        self.secret_count = {}

    def getHint(self, secret: str, guess: str) -> str:
        self.create_secret_count(secret)
        bulls: int = 0
        cows: int = 0
        for guess_index, digit in enumerate(guess):
            if digit in self.secret_count:
                if secret[guess_index] == digit:
                    bulls += 1
                    cows -= 1 if self.secret_count[digit] <= 0 else 0
                else:
                    cows += 1 if self.secret_count[digit] > 0 else 0
                self.secret_count[digit] -= 1

        return self.create_answer(bulls, cows)

    def create_secret_count(self, secret: str) -> Counter:
        self.secret_count = Counter(secret)

    def create_answer(self, bulls: int, cows: int) -> str:
        return f"{bulls}A{cows}B"


if __name__ == '__main__':
    solution = Solution()

    secret = "1807"
    guess = "7810"
    print(solution.getHint(secret, guess))
