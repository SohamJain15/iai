import matplotlib.pyplot as plt

graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [], 'E': [], 'F': []
}
pos = {
 'A': (0, 2),
 'B': (-1, 1), 'C': (1, 1),
 'D': (-1.5, 0), 'E': (-0.5, 0), 'F': (1, 0)
}
values = {'D':3, 'E':5, 'F':2}

def ab(n, isMax, a, b):
    if n in values:
        return values[n], [n]

    best = (-999,[]) if isMax else (999,[])

    for x in graph[n]:
        val, path = ab(x, not isMax, a, b)

        if (isMax and val > best[0]) or (not isMax and val < best[0]):
            best = (val, [n] + path)

        if isMax:
            a = max(a, best[0])
        else:
            b = min(b, best[0])

        if b <= a:
            break   # pruning

    return best

def draw(graph, pos, path):
    for u in graph:
        for v in graph[u]:
            if isinstance(v, tuple): v = v[0]

            x1, y1 = pos[u]
            x2, y2 = pos[v]

            if (u, v) in zip(path, path[1:]):
                plt.plot([x1, x2], [y1, y2], 'r')
            else:
                plt.plot([x1, x2], [y1, y2], 'gray')

    for n in pos:
        x, y = pos[n]

        if n in path:
            plt.scatter(x, y, color='red')
        else:
            plt.scatter(x, y, color='blue')

        plt.text(x, y, n, ha='center')

    plt.title("Graph Path")
    plt.show()            

# -------- RUN --------
value, path = ab('A', True, -999, 999)

print("Optimal Value:", value)
print("Path:", path)

draw(graph, pos, path)