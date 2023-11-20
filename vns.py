import random 
from constants import *
from utils import calculateTotalTardiness, checkFeasibility

random.seed(5)


def VNSSearch(DAG, x0, g, g_params, K, N, I, N_params):
    """
    Generic implementation of a reduced VNS algorithm for the 1|prec|g(.) problem.

    Inputs:
        DAG        -- A dictionary representing the incidence matrix of the directed acyclic graph.
        x0         -- A list containing the initial schedule solution, assumed to always be valid.
        g          -- A cost function (regular measure) for the VNS search algorithm to optimise.
        g_params   -- A list containing input parameters for the cost function.
        K          -- The maximum number of iterations.
        N          -- A neighbourhood generation function.
        I          -- Maximum neighbourhood generation level for VNS.
        N_params   -- A list containing supplementary input parameters for the neighbourhood generation function.  

    Outputs: 
        x, g_best  --  A tuple containing the optimal schedule corresponding to g_best
    """

    k = 0 
    g_best = 0
    x = x0

    while k <= K:
        i = 1 
        while i <= I:
            y = N(DAG, x, i, N_params)
            g_y = g(y, g_params)
            if g_y < g(x, g_params): 
                x = y 
                g_best = g_y
                break 
            else:
                i += 1 
        k += 1 

    return x, g_best


def genSwapIndex(DAG, x): 
    """
    Generates a feasible swap index randomly.

    Inputs:
        DAG  -- A dictionary representing the incidence matrix of the directed acyclic graph
        x    -- A list representing a schedule 
    
    Outputs:
        idx  -- A randomly generated swap index 
    """
    
    idx = random.randint(0, len(x)-2)
    
    # Implementation assumes each random adjacent interchange considered must result in a feasible solution 
    while not checkFeasibility(DAG, x, idx):
        idx = random.randint(0, len(x)-2)

    return idx


def genNeighbour(DAG, x, i, N_params=None): 
    """
    An implementation of a neighbourhood generation function.
    This method begins by randomly determining the number of random swaps in the range [1, i]. 
    Then in each iteration of N_swaps, we randomly generate an index in the range [0, len(y)-2] 
    and apply a feasible adjacent interchange (y[idx], y[idx+1]) to the current solution y.    

    Inputs:
        DAG        -- A dictionary representing the incidence matrix of the directed acyclic graph
        x          -- A list representing a schedule 
        i          -- Maximum number of random adjacent interchanges permitted 
        N_params   -- A list containing supplementary input parameters for the neighbourhood 
                      generation function. Default set to None.   
    
    Outputs:
        y    -- A schedule corresponding to a random point in the neighbourhood of x 
    """

    y = x
    N_swaps = random.randint(1, i)

    for i in range(N_swaps):
        idx = genSwapIndex(DAG, y)
        y = y[:idx] + [y[idx+1], y[idx]] + y[idx+2:]  
    
    return y 


def genNeighbourExtension(DAG, x, i, N_params):
    """
    A refined version of the neighbourhood generation function implementation. 
    After obtaining a random point y in the neighbourhood of x, this function
    attempts to refine the current solution by forcing extra search steps to y.
    If the resulting point found y2 has a strictly lower cost than y then we 
    update y with this solution instead, prior to making the comparison g(y) >= g(x).      

    Inputs:
        DAG        -- A dictionary representing the incidence matrix of the directed acyclic graph
        x          -- A list representing a schedule 
        i          -- Maximum number of random adjacent interchanges permitted 
        N_params   -- A list containing the cost function to optimize, cost function parameters
                      and the number of extra search to perform.  
    
    Outputs:
        y          -- A schedule corresponding to a random point in the neighbourhood of x 
    """

    g, g_params, N_extra_search_steps = N_params[0], N_params[1], N_params[2]
    
    y = genNeighbour(DAG, x, i)
    y2 = genNeighbour(DAG, y, N_extra_search_steps)
    
    if g(y2, g_params) < g(y, g_params):
        y = y2 
    
    return y 


if __name__ == '__main__':
    # Q3.1 - see report for implementation explanation.

    # Q3.2 
    print('Answer for Question 3.2:')
    S, cost = VNSSearch(DAG, x0, calculateTotalTardiness, [p, d], K, genNeighbour, I, [])
    print(f'Optimal schedule found is\n{S}\nwith total tardiness {cost}\n')
    
    # Q3.3
    print('Answer for Question 3.3:')
    S, cost = VNSSearch(DAG, x0, calculateTotalTardiness, [p, d], K, genNeighbourExtension, I, [calculateTotalTardiness, [p, d], 150])
    print(f'Optimal schedule found is\n{S}\nwith total tardiness {cost}\n')
