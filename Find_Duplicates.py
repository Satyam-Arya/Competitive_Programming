def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    result = sorted(list(duplicates))
    return result if result else [-1]

if __name__ == "__main__":
    array = [4, 3, 2, 7, 8, 2, 1, 0]
    result = find_duplicates(array)
    print("Elements occurring more than once:", result)
