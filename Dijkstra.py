class Dijkstra:

    @staticmethod
    def dijkstra_bidirectional_matrix(distances, start_node):
        node_count = len(distances)  # Get node length.
        # Initialize distances and visited flags
        distance = [float('infinity')] * node_count  # Create array with n infinity elements where n is the node count.
        visited = [False] * node_count  # Create an array with n False boolean elements where n is the node count.
        distance[start_node] = 0  # The distance from the start is always set to 0.

        for _ in range(node_count):
            # Initialize min_distance to infinity and min_node to -1.
            # As we go through the nodes, we can keep updating with the smallest values found so far.
            min_distance = float('infinity')
            min_node = -1

            # Go through all notes.
            # For a non-visited node, if it's distance is < min distance, make this the new min distance
            # and keep track of the node.
            for node in range(node_count):
                if not visited[node] and distance[node] < min_distance:
                    min_distance = distance[node]
                    min_node = node

            # Change node's visited status to true.
            visited[min_node] = True

            # Update distances to neighbors
            for neighbor in range(node_count):

                # We have a bidirectional array/table provided for the distances.
                # Check if matrix[i][j] exists, otherwise use matrix[j][i] which is the same.
                if distances[min_node][neighbor] != '':
                    main_distance = distances[min_node][neighbor]
                else:
                    main_distance = distances[neighbor][min_node]

                # Ensure value is a float.
                main_distance = float(main_distance)

                if (not visited[neighbor]) and (main_distance > 0) and (distance[min_node] + main_distance < distance[neighbor]):
                    distance[neighbor] = distance[min_node] + main_distance

        return distance







# Example usage:
# Define a bidirectional distance matrix where matrix[i][j] represents the distance from node i to node j

# start_node = 0
# shortest_distances = dijkstra_bidirectional_matrix(distance_matrix, start_node)
#
# print(shortest_distances)
# print("Shortest Distances from Start Node:")
# for node, distance in enumerate(shortest_distances):
#     print(f"To Node {node}: {distance}")
