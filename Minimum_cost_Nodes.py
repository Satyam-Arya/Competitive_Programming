import heapq

def min_cost_to_connect_ropes(arr):
    if len(arr) < 2:
        return 0  # No cost if there is only one rope

    # Convert the input array into a min-heap
    heapq.heapify(arr)
    total_cost = 0

    # Continue until only one rope is left in the heap
    while len(arr) > 1:
        # Extract the two shortest ropes
        rope1 = heapq.heappop(arr)
        rope2 = heapq.heappop(arr)

        # Connect the ropes and add the cost to the total
        current_cost = rope1 + rope2
        total_cost += current_cost

        # Add the connected rope back to the heap
        heapq.heappush(arr, current_cost)

    return total_cost

ropes = [4, 3, 2, 6]
result = min_cost_to_connect_ropes(ropes)
print("Minimum cost to connect the ropes:", result)
