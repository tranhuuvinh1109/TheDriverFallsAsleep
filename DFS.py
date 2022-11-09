

def DFS(initialState, goal):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(len(frontier) - 1)
        explored.append(state)
        if goal == state:
            return explored
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)
    return


if __name__ == '__main__':
    graph = {
        'A': ['D', 'S'],
        'B': ['S','D', 'E'],
        'C': ['S','E'],
        'D': ['A','B', 'F'],
        'E': ['C', 'B','F','H'],
        'F': ['D', 'E','G'],
        'G': ['F', 'H','B'],
        'H': ['E','G'],
        'S': ['A','B','C'],
    }
    result = DFS('S', 'G')
    if result:
        s = 'explored: '
        for i in result:
            s += i + ' '
            print(s)
    else:
        print("404 Not Found!")