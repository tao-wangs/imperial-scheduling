from collections import deque   
import csv
import random

# Initial Parameters
L = 20
gamma = 10
K = 1000
I = 10 

vii = 17.3270
emboss = 2.2013
muse = 13.3265
night = 21.2220
blur = 5.9509
wave = 9.2330
onnx = 3.8556

x0 = [30, 29, 23, 10, 9, 14, 13, 12, 4, 20, 
      22, 3, 27, 28, 8, 7, 19, 21, 26, 18, 
      25, 17, 15, 6, 24, 16, 5, 11, 2, 1, 31]

d = {1: 172, 2: 82, 3: 18, 4: 61, 5: 93, 6: 71, 
      7: 217, 8: 295, 9: 290, 10: 287, 11: 253, 
      12: 307, 13: 279, 14: 73, 15: 355, 16: 34, 
      17: 233, 18: 77, 19: 88, 20: 122, 21: 71, 
      22: 181, 23: 340, 24: 141, 25: 209, 26: 217, 
      27: 256, 28: 144, 29: 307, 30: 329, 31: 269}

p_real = {1: onnx, 2: muse, 3: emboss, 4: emboss, 5: blur, 6: emboss, 7: vii, 8: blur, 
     9: wave, 10: blur, 11: blur, 12: emboss, 13: onnx, 14: onnx, 15: blur, 
     16: wave, 17: wave, 18: wave, 19: emboss, 20: onnx, 21: emboss, 22: onnx, 23: vii, 
     24: blur, 25: night, 26: muse, 27: emboss, 28: onnx, 29: wave, 30: emboss, 31: muse}

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

random.seed(5) 


def TabuSearch(DAG, x0, g, params, L, gamma, K):
    """
    docstring
    """

    if gamma <= 0: 
        raise Exception('Gamma must be greater than 0.')

    # Initialization
    k = 0 
    tabu_list = deque([], L)
    tabu_list_index = deque([], L)
    accepted_solutions = []
    
    # Assume initial schedule x0 is a valid schedule
    g_best = g(x0, params)
    accepted_solutions.append((x0.copy(), g_best))

    cursor = 0 

    # Local search algorithm
    for k in range(K):
        swap_flag = False 
        g_xk = g(x0, params)
        for _ in range(len(x0)):
            if (x0[cursor],x0[cursor+1]) not in DAG:
                y = x0[:cursor] + [x0[cursor+1], x0[cursor]] + x0[cursor+2:]  
                g_y = g(y, params)
                # print(f'Iteration {k}: currently considering feasible solution {y} with cost {g_y}')
                delta = g_xk - g_y 
                if (delta > -gamma and tuple(sorted([x0[cursor], x0[cursor+1]])) not in tabu_list) or g_y < g_best:
                    x0 = y
                    g_best = min(g_y, g_best)
                    accepted_solutions.append((y, g_y))
                    if tuple(sorted([x0[cursor], x0[cursor+1]])) not in tabu_list:
                        tabu_list.append(tuple(sorted([x0[cursor], x0[cursor+1]])))
                        tabu_list_index.append(k)
                    swap_flag = True
            cursor = (cursor + 1) % (len(x0)-1)
            if swap_flag:
                break
        
        # We might not need this since it implicitly removes the oldest entry
        # However, if g_y < g_best and is tabu, then the tabu_list size will -1 since we still have to remove the oldest pair, right? 
        if k - tabu_list_index[0] > L:
            tabu_list.popleft() 
            tabu_list_index.popleft()

        # Each iteration, we add one pair to the tabu list. 
        # But if it's tabu and strictly less than, we need to add it to the list again? 
        # Can do, but we need to change its index to the new k. 

        if not swap_flag:
            break

    # Removing max size to tabu_list reduces cost to 182, but tabu list is now size 21 rather than 20, violation.
    # for x in accepted_solutions:
    #         print(x)
    

    # print(list(filter(lambda x: x[1] == g_best, accepted_solutions)))

    # print(tabu_list_index)
    # print(len(tabu_list))
    return min(accepted_solutions, key=lambda x: x[1])


def calculateTotalTardiness(x, params):
    """
    Given a schedule x and list of processing times and due dates, 
    calculates the total tardiness of the schedule. 
    """

    p = params[0]
    d = params[1]

    C_i = 0
    T_sum = 0
    for i in range(len(x)):
        C_i += p.get(x[i])
        T_sum += max(0, C_i - d.get(x[i]))

    return T_sum


def calculateTotalWeightedTardiness(x, params):
    """
    Given a schedule x and list of processing times, due dates and weights, 
    calculates the total weighted tardiness of the schedule. 
    """
    
    p, d, w = params[0], params[1], params[2]

    C_i = 0
    wT_sum = 0

    for i in range(len(x)):
        Ci += p.get(x[i])
        wT_sum += w.get(x[i]) * max(0, ci - d.get(x[i]))

    return wT_sum


def solveTutorial3Problem7():
    """
    Solves Problem 7 of Tutorial Sheet 3 to verify correctness of Tabu search algorithm implementation.
    """

    G = {}  # Problem does not involve precedences
    p = {1:10, 2:10, 3:13, 4:4}
    d = {1:4, 2:2, 3:1, 4:12}
    w = {1:14, 2:12, 3:1, 4:12}

    L = 2
    gamma = 100 
    K = 3 

    x0 = [2,1,4,3]

    return TabuSearch(G, x0, calculateTotalWeightedTardiness, [p, d, w], L, gamma, K)


def solveTutorial3Problem8a():
    """
    Solves Problem 8a of Tutorial Sheet 3 to verify correctness of Tabu search algorithm implementation.
    """

    G = {}  # Problem does not involve precedences
    p = {1:16, 2:11, 3:4, 4:8}
    d = {1:1, 2:2, 3:7, 4:9}
    w = {1:3, 2:4, 3:5, 4:7}

    L = 2
    gamma = 20 
    K = 4
    
    x0 = [4,2,1,3]

    return TabuSearch(G, x0, calculateTotalWeightedTardiness, [p, d, w], L, gamma, K)

# print(TabuSearch(G, x0, calculateTotalTardiness, [p_real, d], L, gamma, K))
    
    #Random i swaps 
    #i's valid swaps 
    #check graph for feasibility 

def Experiments(gamma, L):
    """
    
    """
    results = []

    for g in gamma:
        for l in L:
            print(f"Testing Tabu Gamma={g} L={l}")
            print(f"Best result: {TabuSearch(G, x0, calculateTotalTardiness, [p_real, d], l, g, K)}")
            results.append(TabuSearch(G, x0, calculateTotalTardiness, [p_real, d], l, g, K))

    return results

def list_to_csv(filename, integer_list):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(integer_list)

def ConvertCSVs(gamma, L):
    """
    """
    schedules = [list(np.array(s)-1) for s, _ in Experiments(gamma, L)]

    i = 0 
    for g in gamma:
        for l in L:
            list_to_csv(f'tabu_gamma={g}_L={l}.csv', schedules[i])
            i += 1

gamma = [1, 2, 5, 10, 15, 20]
L = [1, 10, 15, 20, 25, 30]
# ConvertCSVs(gamma, L)
Experiments(gamma, L)

# ANSWER FOR QUESTION 2.1 
# print(TabuSearch(G, x0, calculateTotalTardiness, [p, d], L, gamma, K))

# Question 3 R-VNS Search
def VNSSearch(DAG, x0, g, params, K, N, I, N_params):
    """
    """

    k = 0 
    x = x0
    g_best = 0

    while k <= K:
        i = 1 
        while i <= I:
            y = N(DAG, x, i, N_params)
            g_y = g(y, params)
            # print(f'Iteration {k} with max {i} swaps: currently considering feasible solution {y} with cost {g_y}')
            if g_y < g(x, params): 
                x = y 
                g_best = g_y
                break 
            else:
                i += 1 
        k += 1 

    return x, g_best


def checkFeasibility(DAG, x, swapped_idx):
    return (x[swapped_idx], x[swapped_idx+1]) not in DAG


def getSwapIndex(DAG, x): 
    idx = random.randint(0, len(x)-2)
    while not checkFeasibility(DAG, x, idx):
        idx = random.randint(0, len(x)-2)
    return idx

def N(DAG, x, i, N_params=None): 
    y = x
    N_swaps = random.randint(1, i)
    for i in range(N_swaps):
        idx = getSwapIndex(DAG, y)
        y = y[:idx] + [y[idx+1], y[idx]] + y[idx+2:]  
    
    return y 


def N_refined(DAG, x, i, N_params):
    g, g_params = N_params[0], N_params[1]
    y = N(DAG, x, i)
    
    N_last_search_steps = 150
    y2 = N(DAG, y, N_last_search_steps)
    
    if g(y2, g_params) < g(y, g_params):
        y = y2 
    
    return y 

# list_to_csv(f'q3_VNS_schedule.csv', VNSSearch(G, x0, calculateTotalTardiness, [p_real, d], K, N, len(x0), [])[0])
# print(VNSSearch(G, x0, calculateTotalTardiness, [p_real, d], K, N, len(x0), [])
# print(VNSSearch(G, x0, calculateTotalTardiness, [p, d], K, N_refined, len(x0), [calculateTotalTardiness, [p, d]]))


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