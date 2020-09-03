class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        s = []
        for x in range(1,n+1):
            if (x%3 == 0) and (x%5 == 0):
                s.append("FizzBuzz")
            elif x%3 == 0:
                s.append("Fizz")
            elif x%5 == 0:
                s.append("Buzz")
            else:
                s.append(str(x))
        return s