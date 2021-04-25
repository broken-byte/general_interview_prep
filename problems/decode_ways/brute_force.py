

class Decoder:
    def __init__(self):
        self.alphabet_map = {}
        self.encoded_message: str = ""

    def get_number_of_possible_ways_to_decode(self, s: str) -> int:
        self.encoded_message = s
        self.generate_alphabet_map()
        return self.decode_recursively(index=0, length=0)

    def generate_alphabet_map(self):
        self.alphabet_map = {}
        alphabets = range(65, 91)
        digits = range(1, 27)
        for digit, letter in zip(digits, alphabets):
            self.alphabet_map[digit] = chr(letter)

    def decode_recursively(self, index: int, length: int) -> int:
        if self.at_end_of_message(index, length):
            return 1 if self.can_be_decoded(index, length) else 0
        elif self.at_beginning_of_message(index, length) or self.can_be_decoded(index, length):
            single_digit_decoding: int = self.decode_recursively(index + length, 1)
            if self.double_digit_decoding_out_of_bounds(index, length):
                return single_digit_decoding
            else:
                double_digit_decoding: int = self.decode_recursively(index + length, 2)
                return single_digit_decoding + double_digit_decoding
        else:
            return 0

    def at_end_of_message(self, index: int, length: int) -> bool:
        return index + length == len(self.encoded_message)

    def at_beginning_of_message(self, index: int, length: int) -> bool:
        return index == 0 and length == 0

    def double_digit_decoding_out_of_bounds(self, index: int, length: int) -> bool:
        return index + length + 2 > len(self.encoded_message)

    def can_be_decoded(self, index: int, length: int) -> int:
        sub_string = self.encoded_message[index:index + length]
        if sub_string[0] == "0":
            return False
        digit = int(sub_string)
        can_be_decoded: bool = digit in self.alphabet_map
        return can_be_decoded


if __name__ == '__main__':
    decoder = Decoder()
    print(decoder.get_number_of_possible_ways_to_decode("226"))
    print(decoder.get_number_of_possible_ways_to_decode("2125"))
    print(decoder.get_number_of_possible_ways_to_decode("01"))
    print(decoder.get_number_of_possible_ways_to_decode("12"))
    print(decoder.get_number_of_possible_ways_to_decode("0"))
    print(decoder.get_number_of_possible_ways_to_decode("06"))
    print(decoder.get_number_of_possible_ways_to_decode("111111111111111111111111111111111111111111111"))
