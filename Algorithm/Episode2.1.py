"""
<우선순위>
1. 이동한 위치에서 바로 옆에 gate 가 있으면 지운다.
2. shortest + gate 와 연결된 노드 수가 많은 순으로 지운다.
3. gate 의 개수가 같을 경우, gate 와 직접적으로 연결되어 있지 않은 노드 수가 많은 것부터 지운다.
"""
import sys
import math


def floydWarshall(W, P):
    n = len(W)
    D = W
    PI = P
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                PI[i][j] = PI[i][j] if D[i][j] <= D[i][k] + D[k][j] else PI[k][j]
    return D, PI


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

# initialize W
W = [[math.inf for i in range(n)] for j in range(n)]
for i in range(n):
    W[i][i] = 0  # self-node's weight is 0

# initialize P with None.
P = [[None for i in range(n)] for j in range(n)]

# exit gateways list
exit_li = []

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    W[n1][n2] = W[n2][n1] = 1  # undirected node, weight of all nodes is 1
    P[n1][n2] = n1  # mark parent node : n1 -> n2
    P[n2][n1] = n2  # n2 -> n1

for i in range(e):
    ei = int(input())  # the index of a gateway node
    exit_li.append(ei)

W, P = floydWarshall(W, P)  # calculate all pairs shortest paths
####################
for i in range(n):
    print(i, W[i], file=sys.stderr)
print(file=sys.stderr)
for i in range(n):
    print(i, P[i], file=sys.stderr)
print('exit gates', exit_li, file=sys.stderr)
####################

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    # 이동한 위치에서 바로 옆에 gate 가 있으면 지운다.
    finish = False
    for e in exit_li:
        if P[si][e] is not None:
            P[si][e] = P[e][si] = None
            print(si, e)
            finish = True
            break
    if finish is False:
        shortestPath = []
        # shortest path 의 길이를 찾는다.
        shortestLength = math.inf
        for i in range(n):
            if W[si][i] == 0:  # 자기 자신 제외
                continue
            if W[si][i] < shortestLength:
                shortestLength = W[si][i]
        # shortest + gate 와 연결된 노드 수가 많은 순으로 지운다.
        for i in range(n):
            if W[si][i] == shortestLength:
                index = i
                directNodeNum = 0
                exitNode = None
                for e in exit_li:
                    if P[i][e] is not None:
                        directNodeNum += 1
                        if exitNode is None:
                            exitNode = e
                shortestPath.append([index, directNodeNum, exitNode])
        shortestPath = sorted(shortestPath, key=lambda x: x[1], reverse=True)
        print(shortestPath, file=sys.stderr)
        i, j = shortestPath[0][0], shortestPath[0][2]
        P[i][j] = P[j][i] = None
        print(i, j)

