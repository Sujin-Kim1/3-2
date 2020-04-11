import sys
import math

n, l, e = [int(i) for i in input().split()]
ei_list = []  # ei를 담는 matrix
matrix = []  # adjacency matrix
for i in range(n):
    matrix.append([0] * n)
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1
for i in range(e):
    ei = int(input())  # the index of a gateway node
    ei_list.append(ei)
ei_list.sort()
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    loop = True
    for i in ei_list:  # 현재 위치와 gate와 직접적으로 연결된 edge를 먼저 지움
        if matrix[i][si] == 1:
            print(si, i)
            matrix[si][i] = 0
            matrix[i][si] = 0
            loop = False
            break
    if loop:  # 현재 위치와 gate와 연결된 edge가 없음
        # 1. 모든 노드들의 gate와 직접적으로 연결된 edge의 갯수를 구한다.
        # 2. 1.에서 구한 노드들 중 가장 큰 값을 가지는 노드를 구한다.(gate와 연결된 edge의 수가 많은 노드)

        count_list = [0] * n  # 각 노드가 gate랑 연결된 edge의 수가 몇개인지 저장하는 list
        for i in range(n):
            for j in ei_list:
                if matrix[i][j] == 1:
                    count_list[i] += 1
        max_count_node_list = []  # count_list에서 가장 큰 값을 가지는 노드를 저장하는 list
        max_count = max(count_list)
        for i in range(n):
            if count_list[i] == max_count:
                max_count_node_list.append(i)
        depth_matrix = []  # floyd-warshall algorithm의 D(k) matrix
        is_path = []  # undirected graph이므로 한방향으로 통과했는지 확인하는 matix.
        # is_path[i][k]가 1이면 이미 지나왔다는 뜻, 0이면 처음 지나간다는 뜻
        pi_matrix = []  # floyd-warshall algorithm의 π(k) matrix
        for i in range(n):
            depth_matrix.append([100] * n)  # 100은 경로가 없는 것을 나타냄, 즉 floyd-warshall algorithm의 D(k)에서 무한대 값이라고 생각
            pi_matrix.append([100] * n)  # 100은 경로가 없는 것을 나타냄, 즉 floyd-warshall algorithm의 π(k)에서 NIL이라고 생각
            if i in ei_list:
                is_path.append(matrix[i])  # gate에서 일반 node로 지나가는 것을 방지
            else:
                is_path.append([0] * n)
        queue = [si]
        index = 0
        while len(queue) > index:  # depth_matrix, pi_matrix 초기값 설정
            node = queue[index]
            for i in range(n):
                if matrix[node][i] == 1:
                    if is_path[node][i] == 0:
                        depth_matrix[node][i] = 1
                        pi_matrix[node][i] = node
                        is_path[node][i] = 1
                        is_path[i][node] = 1
                        queue.append(i)
            index += 1
        for k in range(n):  # floyd-warshall algorithm
            for i in range(n):
                for j in range(n):
                    if depth_matrix[i][j] >= depth_matrix[i][k] + depth_matrix[k][j]:
                        depth_matrix[i][j] = depth_matrix[i][k] + depth_matrix[k][j]
                        pi_matrix[i][j] = pi_matrix[k][j]
        if len(max_count_node_list) == 1:
            # max_count_node_list에 원소가 1개이면 그냥 그 node와 연결되어 있는 edge중 아무거나 하나 지우면 됨
            gate_connect = max_count_node_list[0]
            for i in ei_list:
                if depth_matrix[gate_connect][i] == 1:
                    print(gate_connect, i)
                    matrix[gate_connect][i] = 0  # 경로를 지우므로 0으로 변경 필요
                    matrix[i][gate_connect] = 0
                    break
        else:
            # max_count_node_list에 원소가 2개 이상일 경우
            not_connect_gate_node_count = []
            # max_count_node_list에 있는 원소들의 경로를 따라가보면서 gate와 만나지 않는 node의 수를 구함
            # gate와 만나지 않는다면 2개 이상인 edge를 지울 기회가 있다는 뜻.
            # gate와 만나지 않는 node의 수가 적다 → 2개 이상인 edge를 지울 기회가 적다.
            # 기회가 적은 노드의 edge부터 지워야함
            for i in max_count_node_list:
                node = i
                count = 0
                while node != si:
                    node = pi_matrix[si][node]
                    decide = True
                    for j in ei_list:
                        if matrix[node][j] == 1:
                            decide = False
                            break
                    if decide:
                        count += 1
                not_connect_gate_node_count.append(count)
            min_count = not_connect_gate_node_count[0]
            min_index = 0
            for i in range(1, len(not_connect_gate_node_count)):  # 기회가 가장 적은 노드를 찾음
                if min_count > not_connect_gate_node_count[i]:
                    min_count = not_connect_gate_node_count[i]
                    min_index = i
            delete_node = max_count_node_list[min_index]
            for i in ei_list:  # 위에서 찾은 노드랑 연결된 edge를 삭제
                if matrix[i][delete_node] == 1:
                    print(delete_node, i)
                    matrix[delete_node][i] = 0
                    matrix[i][delete_node] = 0
                    break
