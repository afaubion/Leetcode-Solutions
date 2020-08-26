class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        currloc = points[0]
        count = 0
        for i in range(1,len(points)):
            while(currloc[0]<points[i][0]) and (currloc[1]<points[i][1]):
                currloc[0]+=1
                currloc[1]+=1
                count+=1
            while(currloc[0]>points[i][0]) and (currloc[1]>points[i][1]):
                currloc[0]-=1
                currloc[1]-=1
                count+=1
            while(currloc[0]<points[i][0]) and (currloc[1]>points[i][1]):
                currloc[0]+=1
                currloc[1]-=1
                count+=1
            while(currloc[0]>points[i][0]) and (currloc[1]<points[i][1]):
                currloc[0]-=1
                currloc[1]+=1
                count+=1
            while(currloc[0]<points[i][0]) and (currloc[1]==points[i][1]):
                currloc[0]+=1
                count+=1
            while(currloc[0]>points[i][0]) and (currloc[1]==points[i][1]):
                currloc[0]-=1
                count+=1
            while(currloc[0]==points[i][0]) and (currloc[1]<points[i][1]):
                currloc[1]+=1
                count+=1
            while(currloc[0]==points[i][0]) and (currloc[1]>points[i][1]):
                currloc[1]-=1
                count+=1
        return count