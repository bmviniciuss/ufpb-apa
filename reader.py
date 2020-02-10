import os
from parser import *


def read_input_file(filename):
  base_dir = os.path.dirname(__file__)
  instance_path = "instancias_teste/"
  file_path = os.path.join(base_dir,  instance_path + filename)

  # read file to memory
  lines = []
  with open(file_path, "rt")as file:
    for line in file:
      lines.append(line.rstrip('\n'))

  #parse initial info
  start = 3
  [name, dimension, capacity] = parse_info(lines[:start])

  # parse demand values
  demand_start_index = start + 1
  demand_end_index = demand_start_index + dimension 
  demands_lines = lines[demand_start_index: demand_end_index]
  demands = parse_demand(demands_lines)

  #cost matrix
  costs_start_index = demand_end_index + 2
  costs_end_index = costs_start_index + dimension
  costs_lines = lines[costs_start_index:costs_end_index]
  costs = parse_costs(costs_lines)

  # clean memory
  del lines

  return [
    name,
    dimension,
    capacity,
    demands,
    costs
  ]
