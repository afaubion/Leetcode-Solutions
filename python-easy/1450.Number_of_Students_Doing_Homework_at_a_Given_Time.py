class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        activestudent = []
        for i in range(0, len(startTime)):
            if (queryTime >= startTime[i]) and (queryTime <= endTime[i]):
                activestudent.append(1)
            else:
                activestudent.append(0)
        count = 0
        for i in activestudent:
            if i == 1:
                count += 1
        return count
