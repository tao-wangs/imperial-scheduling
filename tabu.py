from collections import deque   
import csv
import random
import numpy as np
from constants import *
from utils import calculateTotalTardiness


def TabuSearch(DAG, x0, g, params, L, gamma, K):
    """
    
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
        
        if k - tabu_list_index[0] > L:
            tabu_list.popleft() 
            tabu_list_index.popleft()

        if not swap_flag:
            break

    return min(accepted_solutions, key=lambda x: x[1])


def tabuExperiments(gamma_list, L_list):
    """
    Given a list of gamma and L values, generates an optimal schedule for each combination of gamma and L using Tabu search algorithm. 
    """

    results = []

    for g in gamma_list:
        for l in L_list:
            results.append(TabuSearch(DAG, x0, calculateTotalTardiness, [p_real, d], l, g, K))

    return results


def createTabuExperimentCSVs(gamma_list, L_list):
    """
    Given a list of gamma and L values, generates an optimal schedule for each combination of gamma and L as a csv file. 
    """

    schedules = [list(np.array(s)-1) for s, _ in tabuExperiments(gamma_list, L_list)]

    i = 0 
    for g in gamma:
        for l in L:
            utils.convertListToCSV(f'tabu_gamma={g}_L={l}.csv', schedules[i])
            i += 1


if __name__ == '__main__':
    #Q2.1
    print('Answer for Question 2.1:')
    S, cost = TabuSearch(DAG, x0, calculateTotalTardiness, [p, d], L, gamma, K)
    print(f'Optimal schedule found is\n{S}\nwith total tardiness {cost}\n')
    
    #Q2.2
    print('Answer for Question 2.2:')
    gamma_list = [1, 2, 5, 10, 15, 20]
    L_list = [1, 10, 15, 20, 25, 30]
    schedules = tabuExperiments(gamma_list, L_list)
    x_TS, cost = min(schedules, key=lambda x: x[1])
    print(f'With real processing times, optimal schedule x_TS found is\n{x_TS}\nwith total tardiness {cost}\n')
