from math import inf
from optimizations import reinsertion, swap, two_opt
import copy

def VND(routes, matrix_cost, cost):
  best_routes = copy.deepcopy(routes)
  best_cost = cost
  total = 3
  op = 1

  while op <= total:
    if op == 1:
      reinsertion_cost, reinsertion_routes = reinsertion(best_routes, matrix_cost, best_cost)

      if(reinsertion_cost < best_cost):
        best_cost = reinsertion_cost
        best_routes = reinsertion_routes
      else:
        op += 1
        
    if op == 2:
      two_opt_cost, two_opt_routes = two_opt(best_routes, matrix_cost, best_cost)

      if(two_opt_cost < best_cost):
        best_cost = two_opt_cost
        best_routes = two_opt_routes
      else:
        op += 1

    if op == 3:
      swap_cost, swap_routes = swap(best_routes, matrix_cost, best_cost)

      if(swap_cost < best_cost):
        best_cost = swap_cost
        best_routes = swap_routes
      else:
        op += 1
      
  
  return best_cost, best_routes