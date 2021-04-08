

class Solution:
    def __init__(self):
        self.rotation_map: dict = {}

    def confusingNumber(self, N: int) -> bool:
        self.create_rotation_map_from_0_to_9()
        reconstructed_digit: any = ""
        for digit in reversed(str(N)):
            if self.rotation_map[digit] is None:
                return False
            reconstructed_digit += self.rotation_map[digit]
        return True if N != int(reconstructed_digit) else False

    def create_rotation_map_from_0_to_9(self):
        self.rotation_map = {
            "0": "0",
            "1": "1",
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": "9",
            "7": None,
            "8": "8",
            "9": "6"
        }
