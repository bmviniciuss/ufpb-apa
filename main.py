import sys, os, time
import argparse
from utils import *
from reader import *
from Guloso import Guloso
from datetime import datetime
from optimizations import reinsertion, swap, two_opt
import copy 
import time

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

  ROUNDS = 10
  vmp_costs = []
  vmp_execution_time = []

  vnd_costs = []
  vnd_execution_time = []

  print("File: {} ".format(file_path))
  print("{} Rounds\n".format(ROUNDS))

  for i in range(ROUNDS):
    name, dimension, capacity, nodes, costs = read_input_file(file_path)
    guloso = Guloso(copy.deepcopy(nodes), copy.deepcopy(costs), copy.deepcopy(capacity), copy.deepcopy(dimension))

    vmp_start = time.time()
    guloso_cost, routes = guloso.run()
    vmp_end = time.time()
    vmp_duration = vmp_end - vmp_start
    vmp_execution_time.append(vmp_duration)
    vmp_costs.append(guloso_cost)

    vnd_start = time.time()
    vnd_cost, vnd_routes = VND(copy.deepcopy(routes), copy.deepcopy(costs), copy.deepcopy(guloso_cost))
    vnd_end = time.time()
    vnd_duration = vnd_end - vnd_start
    vnd_execution_time.append(vnd_duration)
    vnd_costs.append(vnd_cost)
    # print("#{}".format(i))
    # print("VMP - Cost:{} - Duration: {:.6f}".format(guloso_cost, vmp_duration))
    # print("VND - Cost:{} - Duration: {:.6f}".format(vnd_cost, vnd_duration))
  
  # VMP stats
  vmp_avg_cost = sum(vmp_costs)/len(vmp_costs)
  vmp_best_cost = min(vmp_costs)
  vmp_avg_execution_time = sum(vmp_execution_time)/len(vmp_execution_time)

  # VND stats
  vnd_avg_cost = sum(vnd_costs)/len(vnd_costs)
  vnd_best_cost = min(vnd_costs)
  vnd_avg_execution_time = sum(vnd_execution_time)/len(vnd_execution_time)

  print("VMP - Avg Cost: {}".format(vmp_avg_cost))
  print("VMP - Best Cost: {}".format(vmp_best_cost))
  print("VMP - Avg Execution Time: {:.6f} seconds".format(vmp_avg_execution_time))

  print("VND - Avg Cost: {}".format(vnd_avg_cost))
  print("VND - Best Cost: {}".format(vnd_best_cost))
  print("VND - Avg Execution Time: {:.6f} seconds".format(vnd_avg_execution_time))





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
