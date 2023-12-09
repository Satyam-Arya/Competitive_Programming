class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_circular_linked_list(head):
    if not head:
        # An empty linked list is considered circular
        return True

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True # There is a cycle

    return False # If the fast pointer reaches the end, there is no cycle

if __name__ == "__main__":
    # Example 1: Circular linked list
    head_circular = ListNode(1)
    head_circular.next = ListNode(2)
    head_circular.next.next = ListNode(3)
    head_circular.next.next.next = head_circular  # Creates a cycle

    result_circular = is_circular_linked_list(head_circular)
    print("Is the linked list circular? (Example 1):", result_circular)

    # Example 2: Linear linked list
    head_linear = ListNode(1)
    head_linear.next = ListNode(2)
    head_linear.next.next = ListNode(3)

    result_linear = is_circular_linked_list(head_linear)
    print("Is the linked list circular? (Example 2):", result_linear)
