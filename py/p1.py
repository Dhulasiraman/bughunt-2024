#program to print a tree pattern with asterisks
# eg :- height = 3
#output :-   *
#           ***
#          *****

def asterisk_tree(height, level):
  if level > height:
    return
  # Print leading spaces to center the asterisks
  spaces = height - level
  for j in range(spaces):
    print(" ", end="")
  # Print the asterisks for the current level
  for j in range(2 * level - 1):
    print("*", end="")
  print()
  # Recursive call for the next level
  asterisk_tree(height, level + 1)

n = int(input("Enter height of tree : "))
asterisk_tree(n, 1)

