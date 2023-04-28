import random

# Define the problem
values = [5, 3, 4, 2]
weights = [4, 2, 3, 1]
capacity = 6
population_size = 10
generations = 5

# Define the genetic algorithm functions
def create_individual():
    return [random.randint(0, 1) for _ in range(len(values))]

def calculate_fitness(individual):
    total_value = sum([individual[i] * values[i] for i in range(len(values))])
    total_weight = sum([individual[i] * weights[i] for i in range(len(weights))])
    if total_weight > capacity:
        return 0
    else:
        return total_value

def select_individuals(population):
    fitnesses = [calculate_fitness(individual) for individual in population]
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        return random.sample(population, 2)
    else:
        probabilities = [fitness / total_fitness for fitness in fitnesses]
        return random.choices(population, weights=probabilities, k=2)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(values) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    mutation_point = random.randint(0, len(values) - 1)
    individual[mutation_point] = 1 - individual[mutation_point]
    return individual

# Define the genetic algorithm
population = [create_individual() for _ in range(population_size)]
for _ in range(generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1, parent2 = select_individuals(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))
    population = new_population

# Find the best individual
best_individual = max(population, key=calculate_fitness)
best_value = calculate_fitness(best_individual)
best_weight = sum([best_individual[i] * weights[i] for i in range(len(weights))])

# Print the result
print(f"Best individual: {best_individual}")
print(f"Best value: {best_value}")
print(f"Best weight: {best_weight}")
