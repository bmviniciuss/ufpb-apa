from math import inf
import copy

def reinsertion(routes, matrix_cost, cost):
  aux_cost = inf
  best_cost = cost
  best_change = (inf, inf)
  new_routes = copy.deepcopy(routes)

  for r in range(len(routes)):
    for i in range(1,len(routes[r])):
      for k in range(i + 1, len(routes[r]) - 1):
        route = routes[r]

        if(k == i +1):
          aux_cost = cost - matrix_cost[route[i-1]][route[i]] - matrix_cost[route[k]][route[k + 1]] + matrix_cost[route[i - 1]][route[k]] + matrix_cost[route[i]][route[k+1]]

        else:
          aux_cost = cost - matrix_cost[route[i-1]][route[i]] - matrix_cost[route[i]][route[i + 1]]  - matrix_cost[route[k]][route[k + 1]]  + matrix_cost[route[i - 1]][route[i + 1]] + matrix_cost[route[k]][route[i]]  + matrix_cost[route[i]][route[k+1]]
       
        if aux_cost <= best_cost:
          best_cost = aux_cost
          new_routes[r] = route
          removed_item = new_routes[r].pop(i)
          new_routes[r].insert(k, removed_item)
          

  return best_cost, new_routes

def swap(routes, matrix_cost, cost):
  aux_cost = inf
  best_cost = cost
  new_routes = copy.deepcopy(routes)


  for r in range(len(routes)):
    for i in range(1,len(routes[r])):
      for k in range(i + 1, len(routes[r]) - 1):
        route = routes[r]

        if k == i + 1:
          aux_cost = cost - matrix_cost[route[i - 1]][route[i]] - matrix_cost[route[k]][route[k + 1]] + matrix_cost[route[i - 1]][route[k]] +matrix_cost[route[i]][route[k + 1]]

        else:
          aux_cost = cost - matrix_cost[route[i - 1]][route[i]] - matrix_cost[route[i]][route[i + 1]] - matrix_cost[route[k - 1]][route[k]] - matrix_cost[route[k]][route[k + 1]] +matrix_cost[route[i - 1]][route[k]] +matrix_cost[route[k]][route[i + 1]] +matrix_cost[route[k - 1]][route[i]] +matrix_cost[route[i]][route[k + 1]]

        if aux_cost < best_cost:
          best_cost = aux_cost
          new_routes[r] = route
          new_routes[r][i], new_routes[r][k] = new_routes[r][k], new_routes[r][i]

  return best_cost, new_routes

def two_opt(routes, matrix_cost, cost):
  aux_cost = inf
  best_cost = cost
  new_routes = copy.deepcopy(routes)


  for r in range(len(routes)):
    for i in range(1,len(routes[r])):
      for k in range(i + 1, len(routes[r]) - 1):
        route = routes[r]

        if k == i + 1:
          aux_cost = cost
        else:
          aux_cost = cost - matrix_cost[route[i-1]][route[i]]- matrix_cost[route[k]][route[k +1]]+ matrix_cost[route[i-1]][route[k]]+ matrix_cost[route[i]][route[k+1]]

        if aux_cost < best_cost:
          best_cost = aux_cost
          new_routes[r] = route[0:i] + route[i: k +1][::-1] + route[k +1 ::]


  return best_cost,new_routes