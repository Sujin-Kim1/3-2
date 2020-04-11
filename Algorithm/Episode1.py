import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
nodes_li = [[] for i in range(n)]  # adjacency matrix
exit_li = []  # exit gateways list
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    nodes_li[n1].append(n2)
    nodes_li[n2].append(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exit_li.append(ei)

x = y = -1
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    while nodes_li[si]:
        isEi = False
        for i in range(len(exit_li)):
            if exit_li[i] in nodes_li[si]:
                isEi = True
                u = nodes_li[si].pop(nodes_li[si].index(exit_li[i]))
                nodes_li[u].remove(si)
                break
        if isEi is False:
            u = nodes_li[si].pop(0)
            nodes_li[u].remove(si)
        x, y = si, u
        print(x, y)
        break
