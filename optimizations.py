from math import inf


def reinsertion(routes, matrix_cost, cost):
  mRemocao = inf
  mInsercao = 0
  auxCost = inf
  mDistancia = cost
  best_change = (inf, inf)

  for r in range(len(routes)):
    for i in range(1,len(routes[r])):
      for k in range(i + 1, len(routes[r]) - 1):
        route = routes[r]
        auxCost = cost -matrix_cost[route[i-1]][route[i]] -matrix_cost[route[i]][route[i + 1]]  -matrix_cost[route[k]][route[k + 1]]  +matrix_cost[route[i - 1]][route[i + 1]]  +matrix_cost[route[k]][route[i]]  +matrix_cost[route[i]][route[k+1]] 


        if auxCost < mDistancia:
          mDistancia = auxCost
          best_change = (i, k)

  return mDistancia

def swap(routes, matrix_cost, cost):
  mRemocao = inf
  mInsercao = 0
  auxCost = inf
  mDistancia = cost
  best_change = (inf, inf)

  for r in range(len(routes)):
    for i in range(1,len(routes[r])):
      for k in range(i + 1, len(routes[r]) - 1):
        route = routes[r]
        auxCost = cost - matrix_cost[route[i-1]][route[i]] - matrix_cost[route[i]][route[i+1]] - matrix_cost[route[k-1]][route[k]] - matrix_cost[route[k]][route[k+1]] + matrix_cost[route[i - 1]][route[k]] + matrix_cost[route[k]][route[i+1]] + matrix_cost[route[k-1]][route[i]] + matrix_cost[route[i]][route[i-1]]

        if auxCost < mDistancia:
          mDistancia = auxCost
          best_change = (i, k)

  return mDistancia

