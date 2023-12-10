from queue import SimpleQueue

def reverse_first_k_elements(queue, k):
    if k <= 0 or k > queue.qsize(): # Invalid value of k
        return

    stack = []

    # Enqueue the first K elements into the stack
    for _ in range(k):
        stack.append(queue.get())

    # Pop the elements from the stack and enqueue them back into the queue
    while stack:
        queue.put(stack.pop())

if __name__ == "__main__":
    q = SimpleQueue()
    for i in range(1, 6):
        q.put(i)

    k = 3  # Number of elements to reverse

    print("Original Queue:")
    while not q.empty():
        print(q.get(), end=" ")

    # Reset the queue for the example
    for i in range(1, 6):
        q.put(i)

    # Reverse the first K elements
    reverse_first_k_elements(q, k)

    print("\nQueue after reversing the first", k, "elements:")
    while not q.empty():
        print(q.get(), end=" ")
