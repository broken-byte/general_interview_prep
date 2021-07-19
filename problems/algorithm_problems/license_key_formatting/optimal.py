

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        s = s .upper()
        size_of_first_group: int = len(s) % k
        first_group: list = [s[:size_of_first_group]]
        other_groups: list = self.split_s_into_size_k_groups(k=k, start_index=size_of_first_group, s=s)
        if size_of_first_group == 0:
            return "-".join(other_groups)
        return "-".join(first_group + other_groups)

    def split_s_into_size_k_groups(self, k: int, start_index: int, s: str) -> list:
        groups: list = []
        for index in range(start_index, len(s), k):
            grouping: str = s[index: index + k]
            groups.append(grouping)
        return groups


if __name__ == '__main__':
    solution = Solution()
    print(solution.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))
    print(solution.licenseKeyFormatting("2-4A0r7-4k", 4))
    print(solution.licenseKeyFormatting("2-5g-3-J", 2))
    print(solution.licenseKeyFormatting("2-4A0r7-4k", 3))
