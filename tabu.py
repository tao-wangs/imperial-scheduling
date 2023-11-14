
# Initial Parameters
L = 20
gamma = 10
x0 = [30, 29, 23, 10, 9, 14, 13, 12, 4, 20, 
      22, 3, 27, 28, 8, 7, 19, 21, 26, 18, 
      25, 17, 15, 6, 24, 16, 5, 11, 2, 1, 31]


def FindAlpha(G, i, alphas, N):
    """
    docstring
    """
    max_alpha = 0
    for j in range(N+1):
        if (i,j) in G:
            max_alpha = max(max_alpha, alphas.get(j, FindAlpha(G, j, alphas, N)))
    
    alphas[i] = max_alpha + 1

    return alphas[i]


def AssignAlphas(G, alphas):
    """
    docstring
    """

    N = max([item for sublist in G.keys() for item in sublist])

    for i in range(N+1):
        if i not in alphas:
            FindAlpha(G, i, alphas, N)

    return alphas    


def TabuSearch(G, p, x0, L, gamma, K):
    """
    docstring
    """

    if gamma <= 0: 
        raise Exception('Gamma must be greater than 0.')

    # Initialization
    alphas = AssignAlphas(G, {})
    k = 0 
    tabu_list = set()
    x_best = x0
    
    # Assume initial schedule x0 is a valid schedule
    g_best = CalculateTotalTardiness(x0)

    # Local search algorithm

    # cursor = 0 
    # If alpha[cursor] < alpha[cursor+1], cursor++ 
    # Else swap and check acceptance threshold

    raise NotImplementedError


def CalculateTotalTardiness(x, p, d):
    """
    docstring
    """

    raise NotImplementedError