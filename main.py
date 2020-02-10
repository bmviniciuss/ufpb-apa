import sys
from utils import *
from reader import *

def main():
  args = sys.argv
  if len(args) > 1 and ".txt" in args[1]:
    filename = args[1]
    [name, dimension, capacity, demands, costs] = read_input_file(filename)

    print("Input:", name)
    print("Dimension:", dimension)
    print("Capacity:", capacity)
    print("\nDemand:")
    print(demands)

    print("\nCosts:")
    print_matrix(costs)
  



if __name__ == "__main__":
    main()
