from Truck import Truck
from math import inf
class Guloso:
  def __init__(self, nodes, cost_matrix, capacity, dimension):
    self.nodes = nodes
    self.cost_matrix = cost_matrix
    self.capacity = capacity
    self.dimension = dimension
    self.trucks = []

  def has_non_visited_nodes(self):
    for node in self.nodes:
      if not node.visited:
        return True
    return False

  def run(self):
    self.trucks.append(Truck(self.capacity))

    final_cost = 0
    visited_cost = 0
    current_truck = 0

    while self.has_non_visited_nodes():
      chosen_index = 0
      chosen_node = None
      min_cost = inf

      if len(self.trucks[current_truck].path) == 0:
        self.trucks[current_truck].add_to_path(self.nodes[0])
        self.nodes[0].visited = True
      
      for i in range(self.dimension):
        if not self.nodes[i].visited:
          if self.trucks[current_truck].available_load() >= self.nodes[i].demand:
            visited_cost = self.cost_matrix[self.trucks[current_truck].current_location][i]
            if visited_cost < min_cost:
              min_cost = visited_cost
              chosen_index = i
              chosen_node = self.nodes[i]
      
      if chosen_node != None:
        truck = self.trucks[current_truck]
        truck.add_to_path(chosen_node)
        truck.add_load(chosen_node.demand)
        truck.current_location = int(chosen_node.id)
        self.nodes[chosen_index].visited = True
        final_cost += min_cost
      else:
        #changing truck
        if int(self.trucks[current_truck].current_location) != 0:
          final_cost += self.cost_matrix[self.trucks[current_truck].current_location][0]
          self.trucks[current_truck].add_to_path(self.nodes[0])
        
        self.trucks.append(Truck(self.capacity))
        current_truck += 1
    return final_cost


