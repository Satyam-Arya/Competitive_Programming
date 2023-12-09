class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list_iterative(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def reverse_linked_list_recursive(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head

if __name__ == "__main__":
    # Construct the linked list
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    # Reverse the linked list iteratively
    reversed_head_iterative = reverse_linked_list_iterative(head)
    
    # Print the reversed linked list (iterative)
    print("Iterative Reversed Linked List:")
    while reversed_head_iterative is not None:
        print(reversed_head_iterative.value, end=" ")
        reversed_head_iterative = reversed_head_iterative.next

    print("\n")

    # Construct the linked list again (as it's modified by the previous function)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    # Reverse the linked list recursively
    reversed_head_recursive = reverse_linked_list_recursive(head)

    # Print the reversed linked list (recursive)
    print("Recursive Reversed Linked List:")
    while reversed_head_recursive is not None:
        print(reversed_head_recursive.value, end=" ")
        reversed_head_recursive = reversed_head_recursive.next
