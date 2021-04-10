from collections import Counter


class Solution:
    def __init__(self):
        self.secret_count = {}
        self.secret = ""
        self.guess = ""
        self.bulls = 0
        self.cows = 0

    def getHint(self, secret: str, guess: str) -> str:
        self.create_secret_count()
        self.secret = secret
        self.guess = guess
        self.look_for_bovines()
        return self.create_answer()

    def create_secret_count(self):
        self.secret_count = Counter(secret)

    def look_for_bovines(self):
        for guess_index, digit in enumerate(self.guess):
            if digit in self.secret_count:
                if self.secret[guess_index] == digit:
                    self.bulls += 1
                    self.cows -= 1 if self.secret_count[digit] <= 0 else 0
                else:
                    self.cows += 1 if self.secret_count[digit] > 0 else 0
                self.secret_count[digit] -= 1

    def create_answer(self) -> str:
        return f"{self.bulls}A{self.cows}B"


if __name__ == '__main__':
    solution = Solution()

    secret = "1807"
    guess = "7810"
    print(solution.getHint(secret, guess))
