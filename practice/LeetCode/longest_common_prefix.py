from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.two_pointers(strs)

    def two_pointers(self, strs: List[str]) -> str:
        prefix = []
        for i, char in enumerate(strs[0]):
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return "".join(prefix)
            prefix.append(char)
        return "".join(prefix)
