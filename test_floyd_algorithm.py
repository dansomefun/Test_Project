import unittest

# from floyd_algo import floyd_algorithm_recursion

class floyd_recursion(unittest.TestCase):
    def shortest_paths(self): 

        # graph 
        INF = float('inf')
        matrix = [

            [0, 3, INF, 5], 
            [2, 0, INF, 4], 
            [INF, 1, 0, INF],
            [INF, INF, 2,0]
        ]

        len_matrix = len(matrix)  # 4

        # floyd_algorithm_recursion(Matrix, len_matrix, len_matrix)

        self.assertEqual(matrix[0][2], 7)
        self.assertEqual(matrix[1][2], 7)

if __name__ == '__main__': 
    unittest.main()
    
    
