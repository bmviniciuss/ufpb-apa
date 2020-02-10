def print_list(my_list):
  for line in my_list:
    print(line)

def print_matrix(matrix):
  for line in matrix:
    for element in line:
      print("{:4}".format(element), end="")
    print()
