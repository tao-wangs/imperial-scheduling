from collections import deque   
import csv
import random
import numpy as np
from constants import *
from utils import calculateTotalTardiness


def TabuSearch(DAG, x0, g, params, L, gamma, K):
    """
    Generic implementation of a tabu search algorithm for the 1|prec|g(.) problem.
    
    Local search rules are implemented according to the instructions from Tutorial Sheet 3:
    - We use an aspiration criterion that always accepts a solution g(y) if g(y) < g_best, even if tabu.
    - We consider adjacent interchanges in positional order. 
    - We increment cyclically the position of the adjacent interchange. 
    - We terminate the algorithm if we "run out" of neighbours. 

    Inputs:
        DAG      -- A dictionary representing the incidence matrix of the direct acyclic graph.
        x0       -- A list containing the initial schedule solution, assumed to always be valid.
        g        -- A cost function (regular measure) for tabu search algorithm to minimise.
        params   -- A list containing parameters for the regular measure function.
        L        -- The maximum size of the tabu list.
        gamma    -- The acceptance threshold for a neighborhood solution.
        K        -- The maximum number of iterations.

    Outputs: 
        A (schedule, cost) tuple containing the optimal schedule corresponding to g_best
    """

    if gamma <= 0: 
        raise Exception('Gamma must be greater than 0.')

    # Initialisation 
    k = 0 
    accepted_solutions = []
    
    # Assume initial schedule x0 is always a valid schedule
    g_best = g(x0, params)
    accepted_solutions.append((x0.copy(), g_best))

    tabu_list = deque([], L)
    # Keeps track of which iteration k the pair was added to the tabu list
    tabu_list_index = deque([], L)

    cursor = 0 

    for k in range(K):
        swap_flag = False 
        g_xk = g(x0, params)
        
        # Search neighbourhood of xk in positional order, starting from cursor index 
        for _ in range(len(x0)):
            # Check if adjacent interchange violates precendences
            if (x0[cursor],x0[cursor+1]) not in DAG:    
                y = x0[:cursor] + [x0[cursor+1], x0[cursor]] + x0[cursor+2:]  
                g_y = g(y, params)
                delta = g_xk - g_y 
                
                # Accept current solution if delta is above acceptance threshold and not adjacent interchange is not 
                # in the tabu list, or aspiration criteria is satisfied
                if (delta > -gamma and tuple(sorted([x0[cursor], x0[cursor+1]])) not in tabu_list) or g_y < g_best:
                    x0 = y
                    g_best = min(g_y, g_best)
                    accepted_solutions.append((y, g_y))
                    
                    # Avoid adding an accepted solution's adjacent interchange that is tabu to the tabu list again
                    if tuple(sorted([x0[cursor], x0[cursor+1]])) not in tabu_list:
                        tabu_list.append(tuple(sorted([x0[cursor], x0[cursor+1]])))
                        tabu_list_index.append(k)
                    swap_flag = True

            # Increment the cursor cyclically such that if adjacent interchange indexes (len(xk)-2, len(xk)-1) was 
            # considered at iteration k, at iteration k+1 the cursor will consider adjacent interchange (0, 1)
            cursor = (cursor+1) % (len(x0)-1)
            
            # Jump to iteration k+1 if we have found an accepted solution
            if swap_flag:
                break
        
        # Remove any pair entry older than L iterations from the tabu list
        if k - tabu_list_index[0] > L:
            tabu_list.popleft() 
            tabu_list_index.popleft()

        # If we cycle through all neighbours and no valid swaps have occurred, terminate the algorithm
        if not swap_flag:
            break
    
    # Retrive the best schedule found which corresponds to the lowest cost g_best
    return min(accepted_solutions, key=lambda x: x[1])


def tabuExperiments(gamma_list, L_list):
    """
    Given two lists of gamma and L values, generates an optimal schedule for each combination of gamma and L\
    using the tabu search implementation.

    Inputs:
        gamma_list  -- A list of gamma values 
        L_list      -- A list of L values 

    Outputs:
        schedules   -- A list of (schedule, cost) tuples for each combination of gamma and L
    """

    schedules = []

    for g in gamma_list:
        for l in L_list:
            schedules.append(TabuSearch(DAG, x0, calculateTotalTardiness, [p_real, d], l, g, K))

    return schedules


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
