import sys, os, time
import argparse
from utils import *
from reader import *
from Guloso import Guloso
from datetime import datetime
from optimizations import reinsertion,swap

def main():
  # Input Parser+
  parser = argparse.ArgumentParser(description='Process tests files')
  parser.add_argument('-f', dest='file_path', help='Path to run single file')
  parser.add_argument('-o', default=False, dest="output", action='store_true')

  args = parser.parse_args()
  file_path = args.file_path
  to_output = args.output


  # if folder_path:
  #   for file in os.listdir(folder_path.split('/')[0]):
  #     if os.path.isfile(os.path.join(folder_path, file)) and "txt" in file:
  #       files.append(file)
  #   files.sort()
  # elif file_path:
  #   files.append(file_path.split('/')[-1])

  # Run
  name, dimension, capacity, nodes, costs = read_input_file(file_path)
  guloso = Guloso(nodes, costs, capacity, dimension)
  guloso_cost, routes = guloso.run()

  reinsertion_cost = reinsertion(routes, costs,guloso_cost)
  swap_cost = swap(routes, costs,guloso_cost)


  print("Test:",file_path)
  print("# Guloso:", guloso_cost)
  print("# Reinsertion:", reinsertion_cost)
  print("# Swap:", swap_cost)

  print()

  if to_output:
    write_to_file(file_path, guloso_cost, reinsertion_cost)


def write_to_file(file_path,guloso_cost, reinsertion_cost):
  file_name = file_path.split('/')[-1].split('.txt')[0]
  output_id = int(datetime.now().timestamp())
  with open("./" + file_name + "_" + str(output_id) + ".txt", "a+") as output_file:
    output_file.write("Test: {}\n".format(file_path))
    output_file.write("# Guloso: {}\n".format(guloso_cost))
    output_file.write("# Reinsertion: {}\n".format(reinsertion_cost))
    output_file.write("\n")



if __name__ == "__main__":
    main()
