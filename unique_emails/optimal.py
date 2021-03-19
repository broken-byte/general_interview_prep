from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        N: len(emails)
        M: length of largest email (bound at 100)
        Time Complexity: O(N*M) -> O(N*100) -> O(N)
        Space Complexity: O(N) -> set uses at most N space
        """
        unique_emails = set()
        for email in emails:  # O(emails)
            local_name, domain_name = self.split_email(email)
            if "+" in local_name:
                local_name = self.get_local_name_after_plus_sign_slice(local_name)  # O(email.length)
            if "." in email:
                local_name = self.get_local_name_minus_several_dots(local_name)  # O(email.length)
            transformed_email = local_name + domain_name
            if transformed_email not in unique_emails:
                unique_emails.add(transformed_email)
        return len(unique_emails)

    def split_email(self, email) -> tuple:
        index_of_at_sign: int = self.get_index_of_at_sign(email)
        local_name = email[:index_of_at_sign]
        domain_name = email[index_of_at_sign:]
        return local_name, domain_name

    @staticmethod
    def get_local_name_after_plus_sign_slice(local_name):  # O(n)
        i = 0
        while local_name[i] != "+":
            i += 1
        sliced_name = local_name[:i]
        return sliced_name  # Could be off by one here

    @staticmethod
    def get_index_of_at_sign(email):
        j = len(email) - 1
        while email[j] != "@":
            j -= 1
        return j

    def get_local_name_minus_several_dots(self, local_name):
        local_name = self.get_local_name_minus_dot(local_name)
        while "." in local_name:
            local_name = self.get_local_name_minus_dot(local_name)
        return local_name

    @staticmethod
    def get_local_name_minus_dot(local_name):
        i = 0
        while i < len(local_name):
            if local_name[i] == ".":
                break
            else:
                i += 1
        return local_name[:i] + local_name[i + 1:]


if __name__ == '__main__':
    s = Solution()
    input = [
        "test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"
    ]
    print(s.numUniqueEmails(input))
