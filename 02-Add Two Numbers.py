# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addNumbers(l1,l2,carryover):
            sum = carryover
            if(l1):
                sum +=l1.val

            if(l2):
                sum +=l2.val

            if(not l1 and not l2 and not carryover):
               return None
            value = sum % 10
            carryover = sum // 10
            next_l1 = l1.next if l1 else None
            next_l2 = l2.next if l2 else None 
            return ListNode(value, next=addNumbers(next_l1,next_l2,carryover))
        return addNumbers(l1,l2,0)
    

def create_list(numbers):
    head = ListNode(numbers[0])
    current = head
    for number in numbers[1:]:
        current.next = ListNode(number)
        current = current.next
    return head

def print_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage
l1 = create_list([2, 4, 3])  # Represents the number 342
l2 = create_list([5, 6, 4])  # Represents the number 465


sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# Print the result
print_list(result)  # Expected output: 7 -> 0 -> 8 -> None (Represents the number 807



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result