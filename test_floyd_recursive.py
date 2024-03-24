
import unittest

from floyd_algo import floyd_algorithm_recursion


class floyd_recursion(unittest.TestCase):
    def test_shortest_paths(self):
        # Example graph
        # G = [
        #     [0, float('inf'), 3, float('inf')],
        #     [2, 0, float('inf'), float('inf')],
        #     [float('inf'), 7, 0, 1],
        #     [6, float('inf'), float('inf'), 0]
        # ]

        INF = float('inf')

        G = [

            [0, 3, INF, 5], 
            [2, 0, INF, 4], 
            [INF, 1, 0, INF],
            [INF, INF, 2,0]
        ]

        n_vertices = len(G)

        # Call the recursive function
        variable_floyd = floyd_algorithm_recursion(G, n_vertices, n_vertices)
                            #  G[1][3]  == 6
        # print("floyd variable: ", variable_floyd)

        # Check if the shortest paths are correctly computed
        # specific assertions here based on your expected results
        print(f"shortest vertex path: {G[0][2]} and we are picking: \n {G[0]} and {G[2]} ")
        self.assertEqual(G[0][2], 7)  # Shortest path from vertex 0 to 2
        self.assertEqual(G[1][3], 4)  # Shortest path from vertex 1 to 3
                        # ('inf', 'inf')
                        #   (6, 'inf')

    

if __name__ == '__main__':
    unittest.main()