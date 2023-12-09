def find_pairs_with_sum(arr, target_sum):
    pairs = []

    seen = set() # Create a set to store seen elements

    for num in arr:
        complement = target_sum - num

        if complement in seen: # Check if the complement is in the seen set
            pairs.append((num, complement))

        seen.add(num)  # Add the current number to the seen set

    return pairs

if __name__ == "__main__":
    array = [1, 0, -4, 5, 6, 9, -2, -3]
    target_sum = 5
    result = find_pairs_with_sum(array, target_sum)

    if result:
        print(f"Pairs with sum {target_sum}: {result}")
    else:
        print(f"No pairs found with sum {target_sum}")
