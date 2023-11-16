from collections import deque   

# Initial Parameters
L = 20
gamma = 10
K = 1000

x0 = [30, 29, 23, 10, 9, 14, 13, 12, 4, 20, 
      22, 3, 27, 28, 8, 7, 19, 21, 26, 18, 
      25, 17, 15, 6, 24, 16, 5, 11, 2, 1, 31]

d = {1: 172, 2: 82, 3: 18, 4: 61, 5: 93, 6: 71, 
      7: 217, 8: 295, 9: 290, 10: 287, 11: 253, 
      12: 307, 13: 279, 14: 73, 15: 355, 16: 34, 
      17: 233, 18: 77, 19: 88, 20: 122, 21: 71, 
      22: 181, 23: 340, 24: 141, 25: 209, 26: 217, 
      27: 256, 28: 144, 29: 307, 30: 329, 31: 269}

p = {1: 3, 2: 10, 3: 2, 4: 2, 5: 5, 6: 2, 7: 14, 8: 5, 
     9: 6, 10: 5, 11: 5, 12: 2, 13: 3, 14: 3, 15: 5, 
     16: 6, 17: 6, 18: 6, 19: 2, 20: 3, 21: 2, 22: 3, 23: 14, 
     24: 5, 25: 18, 26: 10, 27: 2, 28: 3, 29: 6, 30: 2, 31: 10}

G = {(1, 31): 1, (2, 1): 1, (3, 8): 1, (4, 3): 1, (5, 2): 1, (6, 16): 1, 
     (7, 6): 1, (8, 7): 1, (9, 8): 1, (10, 9): 1, (11, 1): 1, (12, 5): 1, 
     (13, 12): 1, (14, 13): 1, (17, 15): 1, (15, 11): 1, (16, 5): 1, 
     (17, 16): 1, (18, 17): 1, (19, 18): 1, (20, 19): 1, (21, 18): 1, 
     (22, 21): 1, (23, 22): 1, (24, 5): 1, (25, 24): 1, (26, 25): 1, 
     (27, 26): 1, (28, 26): 1, (29, 28): 1, (30, 4): 1, (30, 10): 1, 
     (30, 14): 1, (30, 20): 1, (30, 23): 1, (29, 27): 1, (30, 29): 1}


# def FindAlpha(G, i, alphas, N):
#     """
#     docstring
#     """
#     max_alpha = 0
#     for j in range(N+1):
#         if (i,j) in G:
#             max_alpha = max(max_alpha, alphas.get(j, FindAlpha(G, j, alphas, N)))
    
#     alphas[i] = max_alpha + 1

#     return alphas[i]


# def AssignAlphas(G, alphas):
#     """
#     docstring
#     """

#     N = max([item for sublist in G.keys() for item in sublist])

#     for i in range(N+1):
#         if i not in alphas:
#             FindAlpha(G, i, alphas, N)

#     return alphas    


def TabuSearch(G, p, d, x0, L, gamma, K):
    """
    docstring
    """

    if gamma <= 0: 
        raise Exception('Gamma must be greater than 0.')

    # Initialization
    k = 0 
    tabu_list = deque([], L)
    accepted_solutions = []
    
    # Assume initial schedule x0 is a valid schedule
    g_best = CalculateTotalTardiness(x0, p, d)
    accepted_solutions.append((x0.copy(), g_best))

    cursor = 0 

    # Local search algorithm
    for k in range(K):
        swap_flag = False 
        g_xk = CalculateTotalTardiness(x0, p, d)
        for _ in range(len(x0)):
            if (x0[cursor],x0[cursor+1]) not in G:
                y = x0[:cursor] + [x0[cursor+1], x0[cursor]] + x0[cursor+2:]  
                g_y = CalculateTotalTardiness(y, p, d)
                delta = g_xk - g_y
                if (delta > -gamma and (tuple(sorted([x0[cursor], x0[cursor+1]]))) not in tabu_list) or g_y < g_best:
                    x0 = y
                    g_best = min(g_y, g_best)
                    accepted_solutions.append((y, g_y))
                    tabu_list.append((tuple(sorted([x0[cursor], x0[cursor+1]])), k))
                    swap_flag = True
            cursor = (cursor + 1) % (len(x0)-1)
            if swap_flag:
                break
        
        if k - tabu_list[0][1] > L:
            tabu_list.popleft() 

        if not swap_flag:
            break
    

    print(list(filter(lambda x: x[1] == g_best, accepted_solutions)))

    print(tabu_list)
    return min(accepted_solutions, key=lambda x: x[1])


def CalculateTotalTardiness(x, p, d):
    """
    docstring
    """
    C_i = 0
    tardiness = 0
    for i in range(len(x)):
        C_i += p.get(x[i])
        tardiness += max(0, C_i - d.get(x[i]))

    return tardiness

TabuSearch(G, p, d, x0, L, gamma, K)
# print(TabuSearch(G, p, d, x0, L, gamma, K))