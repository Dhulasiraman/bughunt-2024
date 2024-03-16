#program to print an input as the only member of an array everytime the function is called
# input- 1 -> output- [1], input- 2 -> output- [2]

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # Outputs: [1]
print(add_item(2))  # Outputs: [2], not [1, 2]
