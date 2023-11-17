from tabu import TabuSearch

def calculateTotalWeightedTardiness(x, params):
    """
    Given a schedule x and list of processing times, due dates and weights, 
    calculates the total weighted tardiness of the schedule. 
    """

    p, d, w = params[0], params[1], params[2]

    C_i = 0
    wt_sum = 0

    for i in range(len(x)):
        C_i += p.get(x[i])
        wt_sum += w.get(x[i]) * max(0, C_i - d.get(x[i]))

    return wt_sum


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