import sys, os, time
import argparse
from utils import *
from reader import *
from Guloso import Guloso
from datetime import datetime

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

  file_id = int(datetime.now().timestamp())
  with open("./output/" + str(file_id) + "_output.txt", "a+") as output_file:
    for file in files:
      name, dimension, capacity, nodes, costs = read_input_file(mypath + "/" + file)
      guloso = Guloso(nodes, costs, capacity, dimension)
      start_time = time.time()
      guloso_cost = guloso.run()
      end_time = time.time()
      print("Test:",file)
      output_file.write("Test: {}\n".format(file))
      
      print("# Guloso:", guloso_cost)
      output_file.write("# Guloso: {}\n".format(guloso_cost))

      print("# Time: {:f} seconds".format(end_time - start_time) )
      output_file.write("# Time: {:f} seconds\n".format(end_time - start_time) )
      
      print()
      output_file.write("\n")





if __name__ == "__main__":
    main()
