class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        import functools
        nums = (start + 2*i for i in range(n))
        return functools.reduce(lambda a, b: a^b, nums)