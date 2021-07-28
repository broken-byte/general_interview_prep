

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        """
        Time Complexity: O(len(bottom)^2), best guess based
        on the length of bottom being how many triplets we
        need to build a full pyramid on top of the bottom stack

        Space Complexity: O(len(bottom)) for recursive call stack
        """
        allowed_to_char_hash: dict[str: list[str]] = create_allowed_to_char_hash(allowed)

        def can_build_pyramid(current_row: list[str], next_row: list[str], index: int) -> bool:
            # Base Case
            if len(current_row) == 1:
                return True
            # Recursive Cases
            if len(current_row) - len(next_row) == 1:
                can_build: bool = can_build_pyramid(next_row, [], 0)
                if can_build:
                    return True
            else:
                left, right = current_row[index], current_row[index + 1]
                if left not in allowed_to_char_hash:
                    return False
                possible_triples = allowed_to_char_hash[left]
                for triple in possible_triples:
                    if right == triple[1]:
                        can_build = can_build_pyramid(current_row, next_row + [triple[2]], index + 1)
                        if can_build:
                            return True
                return False

        return can_build_pyramid(list(bottom), [], 0)


def create_allowed_to_char_hash(allowed: list[str]) -> dict[str: list[str]]:
    allowed_to_first_char_hash: dict[str: list[str]] = {}
    for triple in allowed:
        first_letter = triple[0]
        if first_letter in allowed_to_first_char_hash:
            allowed_to_first_char_hash[first_letter].append(triple)
        else:
            allowed_to_first_char_hash[first_letter] = [triple]
    return allowed_to_first_char_hash


if __name__ == '__main__':
    solution = Solution()
    print(solution.pyramidTransition(bottom="BCD", allowed=["BCG", "CDE", "GEA", "FFF"]))
    print(solution.pyramidTransition(bottom="AABA", allowed=["AAA", "AAB", "ABA", "ABB", "BAC"]))
    print(solution.pyramidTransition(
        bottom="CCBAD",
        allowed=["AAD", "ACB", "AAC", "AAB", "CDB", "BCB", "BCC", "BAD", "BAB", "BAC", "CAC", "CAB", "CAA", "DCB", "BCD", "ABA", "ABB", "ABC", "BBD", "BBC", "BBB", "ADB", "ADC", "ADA", "DDC", "DDB", "DDD", "CBC", "CBA", "CDA", "CBD", "CDC", "DBA"]
    ))
