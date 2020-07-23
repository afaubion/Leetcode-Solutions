class Solution:
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        return [i for sub in zip(nums[:n], nums[n:]) for i in sub]