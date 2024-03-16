def delete_starting_evens(lst):
    # Find the index of the first odd number
    first_odd_index = 0
    for item in lst:
        if item % 2 == 0:
            first_odd_index += 1
        else:
            break
    # Slice the list from the first odd number to the end
    return lst[first_odd_index:]

# Example usage:
list_example = [2, 8, 10, 11, 12]
print(delete_starting_evens(list_example))
