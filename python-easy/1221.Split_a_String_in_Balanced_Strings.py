class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        countR = 0
        countStr = 0
        temp = []
        for i in s:
            if(i == 'L'):
                countL += 1
                if(countL==countR):
                    temp = []
                    countStr += 1
                temp.append(i)
            if(i == 'R'):
                countR += 1
                if(countL==countR):
                    temp = []
                    countStr += 1
        return countStr