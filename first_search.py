

graph = {
    'A': ["B", "D", "E"],
    'B': ["A", "C"],
    'C': ["B", "E"],
    'D': ["A", "E"],
    'E': ["A", "D", "F", "C"],
    'F': ["E"]
}


def bfs(graph, start):
    queue = []
    queue.append(start)
    result = []
    visited = set()
    visited.add(start)
    while (len(queue) > 0):
        currentVertex = queue.pop(0)
        result.append(currentVertex)
        for neighbor in graph[currentVertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return result


def dfs(graph, start):
    stack = []
    result = []
    stack.append(start)
    visited = set()
    visited.add(start)
    while (len(stack) > 0):
        currentVertex = stack.pop()
        result.append(currentVertex)
        for neighbor in graph[currentVertex]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return result


def deep_first_search(graph, start):
    stack = []
    result = []
    stack.append(start)
    visited = set()
    visited.add(start)
    while (len(stack) > 0):
        currentVertex = stack.pop()
        result.append(currentVertex)
        for neighbor in graph[currentVertex]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return result



print(bfs(graph, 'A'))
print(dfs(graph, 'A'))
