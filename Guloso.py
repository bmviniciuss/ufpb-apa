from Truck import Truck
from math import inf
from random import choice

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
    n_nodes = self.dimension - 1

    while n_nodes > 0:
      chosen_index = 0
      chosen_node = None
      min_cost = inf

      # check if truck path is empty
      if len(self.trucks[current_truck].path) == 0:
        self.trucks[current_truck].add_to_path(self.nodes[0])
        self.nodes[0].visited = True
        if current_truck == 0:
          random_node = None
          while True:
            random_node = choice(self.nodes)
            if self.trucks[current_truck].available_load() >= random_node.demand:
              break

          random_node = choice(self.nodes)
          truck = self.trucks[current_truck]
          prev_location = truck.path[0]
          truck.add_to_path(random_node)
          truck.add_load(random_node.demand)
          truck.current_location = int(random_node.id)
          self.nodes[random_node.id].visited = True
          final_cost += self.cost_matrix[prev_location.id][self.trucks[current_truck].current_location]
          n_nodes -= 1

      
      # run the greedy algorithm
      for i in range(self.dimension):
        if not self.nodes[i].visited:
          if self.trucks[current_truck].available_load() >= self.nodes[i].demand:
            visited_cost = self.cost_matrix[self.trucks[current_truck].current_location][i]
            if visited_cost < min_cost:
              min_cost = visited_cost
              chosen_index = i
              chosen_node = self.nodes[i]


      # if we can choose a node
      if chosen_node != None:
        truck = self.trucks[current_truck]
        truck.add_to_path(chosen_node)
        truck.add_load(chosen_node.demand)
        truck.current_location = int(chosen_node.id)
        self.nodes[chosen_index].visited = True
        final_cost += min_cost
        n_nodes -= 1
      else:
        # Changing truck
        
        if int(self.trucks[current_truck].current_location) != 0:
          final_cost += self.cost_matrix[self.trucks[current_truck].current_location][0]
          self.trucks[current_truck].add_to_path(self.nodes[0])

        self.trucks.append(Truck(self.capacity))
        current_truck += 1

    # taker last truck to the depot
    final_cost += self.cost_matrix[self.trucks[current_truck].current_location][0]
    self.trucks[current_truck].add_to_path(self.nodes[0])

    routes = []

    i = 0
    for truck in self.trucks:
      # print("Truck:", i)
      # print(truck.get_path_ids())
      routes.append(truck.get_path_ids())
      i+=1

    return final_cost, routes

