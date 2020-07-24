class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        for x in J:
            for y in S:
                if x==y:
                    num+=1
        return num