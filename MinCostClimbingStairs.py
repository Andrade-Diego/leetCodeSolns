def minCostClimbingStairs(cost):
    pathCost = 0
    otherPathCost = 0
    for c in cost[::-1]:
        pathCost, otherPathCost = c + min(pathCost, otherPathCost), pathCost
    return min(pathCost, otherPathCost)

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(f"(TEST)\n\tcost of stairs: {cost}\n\tResult: {minCostClimbingStairs(cost)}")
