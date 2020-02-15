class Node:
  def __init__(self, id, demand):
    self._id = int(id)
    self._demand = demand
    self._visited = False

  @property
  def id(self):
    return self._id
  
  @property
  def demand(self):
    return self._demand
  
  @property
  def visited(self):
    return self._visited
  
  @visited.setter
  def visited(self, value):
    self._visited = value

  def __repr__(self):
    return "Node: " + str(self._id)
