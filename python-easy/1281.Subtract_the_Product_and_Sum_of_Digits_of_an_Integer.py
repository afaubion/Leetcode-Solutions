class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod_dig = 1
        sum_dig= 0
        for dig in str(n):
            prod_dig *= int(dig)
        for i in str(n):
            sum_dig += int(i)
        return prod_dig-sum_dig;