def logistic(r, x):
    return r * x * (1 - x)

def vectorization(x0, r, n):
    coord = [(x0,0)]
    for i in range(n):
        y0 = logistic(r, x0)
        coord.append((x0,y0))        
        coord.append((y0,y0))
        x0 = y0
    return coord

