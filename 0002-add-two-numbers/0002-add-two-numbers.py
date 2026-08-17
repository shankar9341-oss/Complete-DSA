class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new1 = ListNode()
        new2 = new1
        rev = 0
        while l1 or l2 or rev:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            val = value1 + value2 + rev

            rev = val // 10
            val = val % 10
            new2.next = ListNode(val)
            new2 = new2.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return new1.next


        