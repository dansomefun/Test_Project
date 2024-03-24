def floyd_warshall_recursive(Matrix, n, k):
    """
    Recursive helper function for the Floyd-Warshall algorithm.
    Computes the shortest paths between all pairs of vertices.

    Args:
        Matrix (list of lists): Weighted graph represented as an adjacency matrix.
        n (int): Number of vertices.
        k (int): Intermediate vertex.

    Returns:
        None (updates the Matrix matrix in-place).
    """
    
    if k == 0:    # should be the base class
        return

    for i in range(n):   #iterating a square with [i][j]
        for j in range(n):
            Matrix[i][j] = min(Matrix[i][j], Matrix[i][k-1] + Matrix[k-1][j])

    def print_solution(Matrix):
        """
        Prints the updated distance matrix.

        Args:
            G (list of lists): Updated distance matrix.
        """
        for row in Matrix:
            print(*row)

    print_solution (Matrix)
    print(f"Calling the recursion function with k = {k}")
    floyd_warshall_recursive(Matrix, n, k-1)



INF = float('inf')


Matrix = [
    [0, INF, 3, INF],
    [2, 0, INF, INF],
    [INF, 7, 0, 1],
    [6, INF, INF, 0]
]

n_vertices = len(Matrix)
floyd_warshall_recursive(Matrix, n_vertices, n_vertices)

# Output the final shortest paths
print("\nFinal shortest paths:")
