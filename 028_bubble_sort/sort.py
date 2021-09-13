# import random

# x = random.sample(range(-200, 150), 50) ## Bonus funkcia  vygeneruje 50 nahodnych cisel z intervalu -200 az 150
x = [5, 2, 3, 1, 4, -1, 3213, 23, 56, -245]

for j in range(len(x) - 1):
    for i in range(len(x) - 1):
        if x[i] > x[i+1] :
            temp = x[i]
            x[i] = x[i+1]
            x[i + 1] = temp
        print(f'Index is: {i} -> {x}')

# print(all(x[i] <= x[i+1] for i in range(len(x)-1))) ## Bonus funkcia vypise True ak je pole usporiadane 