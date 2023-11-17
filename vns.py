import random 
from constants import *
from utils import calculateTotalTardiness

random.seed(5)

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


def genNeighbour(DAG, x, i, N_params=None): 
    y = x
    N_swaps = random.randint(1, i)
    for i in range(N_swaps):
        idx = getSwapIndex(DAG, y)
        y = y[:idx] + [y[idx+1], y[idx]] + y[idx+2:]  
    
    return y 


def genNeighbourExtension(DAG, x, i, N_params):
    g, g_params = N_params[0], N_params[1]
    y = genNeighbour(DAG, x, i)
    
    N_last_search_steps = 150 # This should be a parameter
    y2 = genNeighbour(DAG, y, N_last_search_steps)
    
    if g(y2, g_params) < g(y, g_params):
        y = y2 
    
    return y 


if __name__ == '__main__':
    #Q3.1 see report. 

    #Q3.2 
    print('Answer for Question 3.2:')
    S, cost = VNSSearch(DAG, x0, calculateTotalTardiness, [p, d], K, genNeighbour, I, [])
    print(f'Optimal schedule found is\n{S}\nwith total tardiness {cost}\n')
    
    #Q3.3
    print('Answer for Question 3.3:')
    S, cost = VNSSearch(DAG, x0, calculateTotalTardiness, [p, d], K, genNeighbourExtension, I, [calculateTotalTardiness, [p, d]])
    print(f'Optimal schedule found is\n{S}\nwith total tardiness {cost}\n')
