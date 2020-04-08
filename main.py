import sys, os, time
import argparse
from utils import *
from reader import *
from Guloso import Guloso
from datetime import datetime
from optimizations import reinsertion, swap, two_opt
import copy 

from VND import VND

def main():
  # Input Parser+
  parser = argparse.ArgumentParser(description='Process tests files')
  parser.add_argument('-f', dest='file_path', help='Path to run single file')
  parser.add_argument('-o', default=False, dest="output", action='store_true')

  args = parser.parse_args()
  file_path = args.file_path
  to_output = args.output

  # Run
  name, dimension, capacity, nodes, costs = read_input_file(file_path)
  guloso = Guloso(nodes, costs, capacity, dimension)
  guloso_cost, routes = guloso.run()

  reinsertion_cost, reinsertion_routes = reinsertion(copy.deepcopy(routes), copy.deepcopy(costs),copy.deepcopy(guloso_cost))
  swap_cost, swap_routes = swap(copy.deepcopy(routes), copy.deepcopy(costs),copy.deepcopy(guloso_cost))

  two_opt_cost, two_opt_routes = two_opt(copy.deepcopy(routes), costs,copy.deepcopy(guloso_cost))
  vnd_cost, vnd_routes = VND(copy.deepcopy(routes), copy.deepcopy(costs), copy.deepcopy(guloso_cost))

  print("Test:",file_path)
  print("# VMP:", guloso_cost)
  print("# Reinsertion:", reinsertion_cost)
  print("# Swap:", swap_cost)
  print("# Two-Opt:", two_opt_cost)
  print("# VND:", vnd_cost)
  print()

  if to_output:
    write_to_file(file_path, guloso_cost, reinsertion_cost)


def write_to_file(file_path,guloso_cost, reinsertion_cost, swap_cost, two_opt_cost, vnd_cost):
  file_name = file_path.split('/')[-1].split('.txt')[0]
  output_id = int(datetime.now().timestamp())
  with open("./" + file_name + "_" + str(output_id) + ".txt", "a+") as output_file:
    output_file.write("Test: {}\n".format(file_path))
    output_file.write("# VMP: {}\n".format(guloso_cost))
    output_file.write("# Reinsertion: {}\n".format(reinsertion_cost))
    output_file.write("# Swap: {}\n".format(swap_cost))
    output_file.write("# Two-Opt: {}\n".format(two_opt_cost))
    output_file.write("# VND: {}\n".format(vnd_cost))


    output_file.write("\n")



if __name__ == "__main__":
    main()
