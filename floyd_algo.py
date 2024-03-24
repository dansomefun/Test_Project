

def floyd_algorithm_recursion(Matrix, n, k): 
    
    # BASE CASE  --> avoid infinite looping 
    if k == 0: 
        return 

    # #return all possible paths and find the minimum
    # distance[start_node][end_node] = min(distance[start_node][end_node],
    # distance[start_node][intermediate] + distance[intermediate][end_node] )

    for i in range(n): 
        for j in range(n): 
            Matrix[i][j] = min(Matrix[i][j], Matrix[i][k-1] + Matrix[k-1][j])

     # operation to be done 
    # print(n)  # operation
            #                [0, 3, INF, 5] 
            #                [2, 0, INF, 4], 
            #                [INF, 1, 0, INF],
            #                [INF, INF, 2,0]

    operation(Matrix)
    
    print("the matrix number: ", k)  # -> k = 1
    # recursive function  
    floyd_algorithm_recursion(Matrix, n, k-1)


def operation(Matrix):
        for row in Matrix: 
            print(*row)

INF = float('inf')
Matrix = [

    [0, 3, INF, 5], 
    [2, 0, INF, 4], 
    [INF, 1, 0, INF],
    [INF, INF, 2,0]
]

print("length of matrix", len(Matrix))
len_matrix = len(Matrix)
        
floyd_algorithm_recursion(Matrix, len_matrix, len_matrix)




