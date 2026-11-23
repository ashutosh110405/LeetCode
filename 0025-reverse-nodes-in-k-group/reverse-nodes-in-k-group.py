from typing import Optional

# Note: ListNode is provided by LeetCode. Do not include it in your submission.
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse the k nodes in the current group
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Connect previous group to the new head (kth) and advance group_prev
            new_group_tail = group_prev.next
            group_prev.next = kth
            group_prev = new_group_tail