import numpy as np
import matplotlib.pyplot as plt

# simple fitness function (maximize x^2)
def fitness(x):
    return x * x

# initial population
pop = np.random.uniform(-10, 10, 10)

history = []

for i in range(20):  # generations

    fit = fitness(pop)
    history.append(max(fit))

    # select best half
    idx = np.argsort(fit)[-5:]
    parents = pop[idx]

    # create new population
    new_pop = []

    for j in range(10):
        p1, p2 = np.random.choice(parents, 2)
        child = (p1 + p2) / 2
        new_pop.append(child)

    pop = np.array(new_pop)

# final best answer
print("Best value:", pop[np.argmax(fitness(pop))])

# graph
plt.plot(history)
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Genetic Algorithm")
plt.grid()
plt.show()