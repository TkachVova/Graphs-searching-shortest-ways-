import operator

graph = {'A': [['B', 'C'], [2, 3]],
         'B': [['A', 'D', 'E'], [2, 1, 5]],
         'C': [['A', 'F'], [3, 4]],
         'D': [['B'], [1]],
         'E': [['B', 'F'], [5, 1]],
         'F': [['C', 'E'], [4, 1]]}


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in set(graph[start][0]) - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex][0]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def numbOfElem(a, lst):
    for i in range(len(lst)):
        if lst[i] == a:
            return i

def calculate_shortest(lst, graph):
    min = -1
    curr = 0
    currlist = 0
    for l in lst:
        for i in range(len(l)-1):
            curr += graph[l[i]][1][numbOfElem(l[i+1], list(graph[l[i]][0]))]
        if min == -1:
            min = curr
            currlist = l
        if min > curr:
            min = curr
            currlist = l
        curr = 0
    return str(min) + " " +str(currlist)



def depth_first(graph, a, b):
    x = list(dfs_paths(graph, a, b))
    return calculate_shortest(x, graph)

def breadth_first(graph, a, b):
    x = list(bfs_paths(graph, a, b))
    return calculate_shortest(x, graph)



def degree(a, graph):
    return len(graph[a][0])

def nodes_list(graph):
    degrees = []
    dict = {}
    for i in graph:
        dict[i] = degree(i, graph)
    sortedGraph = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    return sortedGraph

print("depth_first")
print(depth_first(graph, 'A', 'F'))

print("breadth-first")
print(breadth_first(graph, 'A', 'F'))

print("Nodes_list")

print(nodes_list(graph))
