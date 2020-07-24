class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = []
        val = 0
        for i in nums:
            for j in nums:
                if j<i:
                    val+=1
            temp.append(val)
            val = 0
        return temp