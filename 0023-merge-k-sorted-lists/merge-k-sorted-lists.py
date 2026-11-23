import heapq
from typing import List, Optional

# Note: ListNode is provided by LeetCode. Do not include it in your submission.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for idx, node in enumerate(lists):
            if node is not None:
                heapq.heappush(min_heap, (node.val, idx, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            _, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next