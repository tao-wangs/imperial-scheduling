

def FindAlpha(G, i, alphas, N):
        max_alpha = 0
        for j in range(N+1):
            if (i,j) in G:
                max_alpha = max(max_alpha, alphas.get(j, FindAlpha(G, j, alphas, N)))
        
        alphas[i] = max_alpha + 1
        return alphas[i]

def AssignAlphas(G, alphas):
    N = max([item for sublist in G.keys() for item in sublist])

    for i in range(N+1):
        if i not in alphas:
            FindAlpha(G, i, alphas, N)

    return alphas    
