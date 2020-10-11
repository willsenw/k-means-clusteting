import matplotlib.pyplot as plt
import numpy as np
import math

def getColor( nc ) :
    if nc == 3 :
        return 'pink'
    elif nc == 2 :
        return 'yellow'
    elif nc == 1 :
        return 'red'
    elif nc == 0 :
        return 'blue'
    else:
        return 'green'

def dist( pta, ptb ):
    x = pta[0] + ptb[0]
    y = pta[1] + ptb[1]
    return math.sqrt(x*x+y*y)

N = 200
K = 5
it = 100

np.random.seed(25041996)
data = np.random.randn(3, N)

fig, axs = plt.subplots(1,1, figsize=(5, 5))
for i in range(N):
    data[0][i] = (data[0][i] * 512)
    data[1][i] = (data[1][i] * 473)
    data[2][i] = (int)(0)
centroid = [ [data[0][i],data[1][i]] for i in range(K)]

changes = True
while changes == True and it > 0:
    it -= 1
    changes = False
    for i in range(N):
        opt = (int)(data[2][i])
        temp = [data[0][i],data[1][i]]
        for k in range(K):
            if dist(centroid[k], temp) < dist(centroid[opt], temp):
                opt = (int)(k)
        if opt != (int)(data[2][i]) :
            data[2][i] = (int)(opt)
            changes = True

    if changes == True :
        for k in range(K):
            x = 0
            y = 0
            n = 0
            for i in range(N):
                if (int)(data[2][i]) == k:
                    x += data[0][i]
                    y += data[1][i]
                    n += 1
            if n > 0 :
                x //= n
                y //= n
            centroid[k] = [x,y]

for i in range(N):
    axs.scatter(data[0][i], data[1][i], color=getColor(data[2][i]))
plt.show()