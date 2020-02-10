def parse_info(lines):
  info = []
  for line in lines:
    [key,value] = [a.strip() for a in line.split(":")]
    if key == "NAME":
      info.append(value)
      
    if key in ["CAPACITY", "DIMENSION"]:
      info.append(int(value))
  return info

def parse_demand(lines):
  demands = []
  for line in lines:
    [index, demand] = [a.strip() for a in line.split()]
    demands.append(int(demand))

  return demands

def parse_costs(lines):
  costs = []
  for line in lines:
    parsed = [int(l) for l in line.split()]
    costs.append(parsed)
  return costs
