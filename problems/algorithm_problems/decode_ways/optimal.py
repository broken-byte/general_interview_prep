

class Decoder:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def __init__(self):
        self.encoded_message: str = ""
        self.memo: dict = {}

    def numDecodings(self, s: str) -> int:
        self.encoded_message = s
        self.memo = {}
        return self.decode_recursively(0)

    def decode_recursively(self, index) -> int:
        if index in self.memo:
            return self.memo[index]
        elif self.at_end_of_message(index):
            return 1
        elif self.has_leading_zero(index):
            return 0
        elif self.one_of_from_end_of_message(index):
            return 1
        else:
            num_decodes = self.decode_recursively(index + 1)
            if self.double_digit_can_be_decoded(index):
                num_decodes += self.decode_recursively(index + 2)
            self.memo[index] = num_decodes
            return num_decodes

    def at_end_of_message(self, index: int) -> bool:
        return index == len(self.encoded_message)

    def has_leading_zero(self, index: int) -> bool:
        return self.encoded_message[index] == '0'

    def one_of_from_end_of_message(self, index: int) -> bool:
        return index == len(self.encoded_message) - 1

    def double_digit_can_be_decoded(self, index: int) -> bool:
        sub_message: str = self.encoded_message[index: index + 2]
        double_digit_decode = int(sub_message)
        return double_digit_decode <= 26


if __name__ == '__main__':
    decoder = Decoder()
    print(decoder.numDecodings("226"))
    print(decoder.numDecodings("2125"))
    print(decoder.numDecodings("01"))
    print(decoder.numDecodings("12"))
    print(decoder.numDecodings("0"))
    print(decoder.numDecodings("06"))
    print(decoder.numDecodings("1111111111111111111111"))
