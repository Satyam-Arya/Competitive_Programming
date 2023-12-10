def remove_duplicates(input_string):
    seen = set()
    result = []

    for char in input_string:
        if char not in seen:
            result.append(char)
            seen.add(char)

    return ''.join(result)

input_str = "_remove_duplicates_"
result_str = remove_duplicates(input_str)
print("String after removing duplicates:", result_str)