from math import inf


def reinsertion(routes, matrix_cost, cost):
  aux_cost = inf
  best_cost = cost
  best_change = (inf, inf)

  for r in range(len(routes)):
    for i in range(1,len(routes[r])):
      for k in range(i + 1, len(routes[r]) - 1):
        route = routes[r]
        aux_cost = cost -matrix_cost[route[i-1]][route[i]] -matrix_cost[route[i]][route[i + 1]]  -matrix_cost[route[k]][route[k + 1]]  +matrix_cost[route[i - 1]][route[i + 1]]  +matrix_cost[route[k]][route[i]]  +matrix_cost[route[i]][route[k+1]] 


        if aux_cost < best_cost:
          best_cost = aux_cost
          best_change = (i, k)

  return best_cost

def swap(routes, matrix_cost, cost):
  aux_cost = inf
  best_cost = cost
  best_change = (inf, inf)

  for r in range(len(routes)):
    for i in range(1,len(routes[r])):
      for k in range(i + 1, len(routes[r]) - 1):
        route = routes[r]
        aux_cost = cost - matrix_cost[route[i-1]][route[i]] - matrix_cost[route[i]][route[i+1]] - matrix_cost[route[k-1]][route[k]] - matrix_cost[route[k]][route[k+1]] + matrix_cost[route[i - 1]][route[k]] + matrix_cost[route[k]][route[i+1]] + matrix_cost[route[k-1]][route[i]] + matrix_cost[route[i]][route[i-1]]

        if aux_cost < best_cost:
          best_cost = aux_cost
          best_change = (i, k)

  return best_cost

def two_opt(routes, matrix_cost, cost):
  aux_cost = inf
  best_cost = cost
  best_change = (inf, inf)

  for r in range(len(routes)):
    for i in range(1,len(routes[r])):
      for k in range(i + 1, len(routes[r]) - 1):
        route = routes[r]
        aux_cost = cost - matrix_cost[route[i-1]][route[i]]- matrix_cost[route[k]][route[k +1]]+ matrix_cost[route[i-1]][route[k]]+ matrix_cost[route[i]][route[k+1]]

        if aux_cost < best_cost:
          best_cost = aux_cost
          best_change = (i, k)

  return best_cost