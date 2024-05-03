import csv
import numpy as np
import time
from memory_profiler import memory_usage

# Function to implement Floyd's algorithm using a 2D array
def floyd(graph):
    nodes = len(graph)
    distance = np.copy(graph)
    parent = np.zeros((nodes, nodes), dtype=int)

    for i in range(nodes):
        for j in range(nodes):
            if i != j and graph[i][j] != float('inf'):
                parent[i][j] = i
            else:
                parent[i][j] = -1

    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    parent[i][j] = parent[k][j]

    return distance, parent

# Function to find the shortest path using the parent matrix
def find_path(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[start][path[-1]])
    path.reverse()
    return path

# Read the CSV file and build the graph using a 2D array
def read_csv_to_graph(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header
        max_node_id = -1

        for row in csv_reader:
            node_id, connected_node_id, distance = map(int, row[:3])
            max_node_id = max(max_node_id, node_id, connected_node_id)

        graph = np.full((max_node_id + 1, max_node_id + 1), float('inf'))
        csv_file.seek(0)
        next(csv_reader)  # Skip the header

        for row in csv_reader:
            node_id, connected_node_id, distance = map(int, row[:3])
            graph[node_id][connected_node_id] = distance

        return graph

# Main function to find and print the shortest path
def main():
    csv_file = "Project2_Input_File14.csv"  # Replace with your CSV file path
    start = 138
    end = 66

    start_time = time.time()
    mem_usage_before = memory_usage()[0]

    graph = read_csv_to_graph(csv_file)
    distances, parents = floyd(graph)
    path = find_path(parents, start, end)

    end_time = time.time()
    mem_usage_after = memory_usage()[0]

    print(f"Shortest path from node {start} to node {end}: {path}")
    print(f"Total distance: {distances[start][end]}")
    print(f"Execution time: {end_time - start_time} seconds")
    print(f"Memory usage: {mem_usage_after - mem_usage_before} MiB")

if __name__ == "__main__":
    main()