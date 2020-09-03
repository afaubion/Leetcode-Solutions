# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iteratively
def reverseList1(self, head):
    node = None
    while head:
        tmp = head.next
        head.next = node
        node = head
        head = tmp
    return node


# Recursively
def reverseList(self, head):
    return self.helper(head, None)


def helper(self, head, node):
    if not head:
        return node
    tmp = head.next
    head.next = node
    return self.helper(tmp, head)