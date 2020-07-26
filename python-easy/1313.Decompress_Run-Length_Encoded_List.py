from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            res += [nums[i+1]] * nums[i]
        return res

def main():
    temp = [42, 39]
    another = [1,2,3,4]
    x = Solution()
    print(x.decompressRLElist(temp))
    print(x.decompressRLElist(another))



if __name__ == '__main__':
    main()
