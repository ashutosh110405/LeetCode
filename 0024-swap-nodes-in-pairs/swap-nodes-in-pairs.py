class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to act as the prev node for the first pair
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev pointer two nodes forward
            prev = first
            
        return dummy.next