import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    priority_queue = [(0, start_node)]

    while priority_queue:
        curr_dist, curr_node = heapq.heappop(priority_queue)

        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return distances

graph_data = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 2), ('C', 3), ('D', 5)],
    'C': [('A', 4), ('B', 3), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
start = 'A'
distances_result = dijkstra(graph_data, start)
print(distances_result)  # Output: {'A': 0, 'B': 1, 'C': 4, 'D': 5}