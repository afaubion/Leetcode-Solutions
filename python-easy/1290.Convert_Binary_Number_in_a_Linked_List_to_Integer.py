# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # convert list to array
        curr = head
        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next
        # -----------------------------
        # travel array from en to beginning.
        # if bit is 1 then add to the result, 2 raised to the position power starting at 0 for the right en bit
        result = 0
        pw = 0

        curr_bit = len(arr) - 1

        while curr_bit >= 0:
            if arr[curr_bit] == 1:
                result += 2 ** pw

            pw += 1
            curr_bit -= 1

        return result



