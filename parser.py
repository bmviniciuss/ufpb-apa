from Node import Node

def parse_info(lines):
  info = []
  for line in lines:
    [key,value] = [a.strip() for a in line.split(":")]
    if key == "NAME":
      info.append(value)
      
    if key in ["CAPACITY", "DIMENSION"]:
      info.append(int(value))
  return info

def parse_nodes(lines):
  nodes = []
  for line in lines:
    [index, demand] = [a.strip() for a in line.split()]
    nodes.append(Node(index, int(demand)))

  return nodes

def parse_costs(lines):
  costs = []
  for line in lines:
    parsed = [int(l) for l in line.split()]
    costs.append(parsed)
  return costs
