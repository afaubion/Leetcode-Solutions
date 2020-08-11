class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_txt = [0] * len(indices)
        j = 0
        for i in indices:
            new_txt[i] = s[j]
            j = j + 1
        return ''.join(new_txt)
