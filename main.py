import sys, os, time
import argparse
from utils import *
from reader import *
from Guloso import Guloso

def main():
  # Input Parser
  parser = argparse.ArgumentParser(description='Process tests files')
  parser.add_argument('-p', dest='path', help='Directory path for test files')
  args = parser.parse_args()
  mypath = args.path

  files = []
  for file in os.listdir(mypath):
    if os.path.isfile(os.path.join(mypath, file)) and "txt" in file:
      files.append(file)
  
  files.sort()

  for file in files:
    name, dimension, capacity, nodes, costs = read_input_file(mypath + "/" + file)
    guloso = Guloso(nodes, costs, capacity, dimension)
    start_time = time.time()
    guloso_cost = guloso.run()
    end_time = time.time()
    print("Test:",file)
    print("# Guloso:", guloso_cost)
    print("# Time: {:f} seconds".format(end_time - start_time) )
    print()





if __name__ == "__main__":
    main()
