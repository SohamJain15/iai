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

def bfs(s, g):
    q = [[s]]

    while q:
        p = q.pop(0)   # FIFO

        if p[-1] == g:
            return p

        for n in graph[p[-1]]:
            q.append(p + [n])


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
bfs_path = bfs('A', 'D')
print("BFS Path:", bfs_path)

draw(graph, pos, bfs_path)