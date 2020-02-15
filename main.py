import sys
from utils import *
from reader import *
from Guloso import Guloso

def main():
  args = sys.argv
  if len(args) > 1 and ".txt" in args[1]:
    filename = args[1]
    name, dimension, capacity, nodes, costs = read_input_file(filename)

    if len(args) > 2 and args[2] in ["--debug", "-d"]:
      print("entrou")
      print("Input:", name)
      print("Dimension:", dimension)
      print("Capacity:", capacity)
      print("\nDemand:")
      print(demands)

      print("\nCosts:")
      print_matrix(costs)

    guloso = Guloso(nodes, costs, capacity, dimension)
    guloso_cost = guloso.run()
    print("Guloso:", guloso_cost)



if __name__ == "__main__":
    main()
