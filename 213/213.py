# Project Euler 213
N = 30
jumps = []

for i in range(N * N):
    jump = []
    if i % N > 0:
        jump.append(i - 1)
    if i % N < N - 1:
        jump.append(i + 1)
    if i >= N:
        jump.append(i - N)
    if i < N * (N - 1):
        jump.append(i + N)
    jumps.append(jump)

fleas = []

for i in range(N * N):
    flea = [0] * N * N
    flea[i] = 1.0
    fleas.append(flea)

def boxp(N, fleas):
    boxes = [1.0] * N * N
    for flea in fleas:
        for i in range(N * N):
            boxes[i] *= (1 - flea[i])
    return boxes

for bell in range(50):
    newfleas = []
    for flea in fleas:
        newflea = [0] * N * N
        for box, jump in enumerate(jumps):
            x = flea[box] / float(len(jump))
            for j in jump:
                newflea[j] += x
        newfleas.append(newflea)
    fleas = newfleas
        
print round(sum(boxp(N, fleas)), 6)
