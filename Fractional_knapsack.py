class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.value_per_weight = value / weight

def fractional_knapsack(items, capacity):
    # Sort items based on value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x.value_per_weight, reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for item in sorted_items:
        if remaining_capacity >= item.weight:
            # Take the entire item
            total_value += item.value
            remaining_capacity -= item.weight
        else:
            # Take a fraction of the item to fill the remaining capacity
            fraction = remaining_capacity / item.weight
            total_value += fraction * item.value
            remaining_capacity = 0

        if remaining_capacity == 0:
            break

    return total_value

if __name__ == "__main__":
    items = [Item(value=60, weight=10), Item(value=100, weight=20), Item(value=120, weight=30)]
    knapsack_capacity = 50
    result = fractional_knapsack(items, knapsack_capacity)
    print(f"The maximum total value in the knapsack is: {result}")
