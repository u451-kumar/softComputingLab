import random

# Define the items and their values and weights
items = [("item1", 10, 2), ("item2", 5, 3), ("item3", 15, 5), ("item4", 7, 7), ("item5", 6, 1)]

# Define the maximum weight the knapsack can hold
max_weight = 10

# Define the genetic algorithm parameters
pop_size = 10  # population size
elite_size = 2  # number of elite individuals to pass to the next generation
mutation_rate = 0.1  # mutation rate

def fitness(individual):
    """Calculate the fitness of an individual."""
    value = sum([item[1] * gene for item, gene in zip(items, individual)])
    weight = sum([item[2] * gene for item, gene in zip(items, individual)])
    if weight > max_weight:
        return 0
    else:
        return value

def create_individual():
    """Create a random individual."""
    return [random.randint(0, 1) for _ in range(len(items))]

def create_population():
    """Create a population of random individuals."""
    return [create_individual() for _ in range(pop_size)]

def crossover(parent1, parent2):
    """Perform a single-point crossover between two parents."""
    crossover_point = random.randint(1, len(items) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    """Mutate an individual."""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def select_individuals(population):
    """Select elite individuals to pass to the next generation."""
    return sorted(population, key=fitness, reverse=True)[:elite_size]

def breed_population(elite):
    """Breed a new population from the elite individuals."""
    offspring = []
    while len(offspring) < pop_size:
        parent1 = random.choice(elite)
        parent2 = random.choice(elite)
        child1, child2 = crossover(parent1, parent2)
        offspring.append(mutate(child1))
        if len(offspring) < pop_size:
            offspring.append(mutate(child2))
    return offspring

def genetic_algorithm():
    """Perform the genetic algorithm."""
    population = create_population()
    for i in range(100):
        elite = select_individuals(population)
        population = breed_population(elite)
    best_individual = max(population, key=fitness)
    best_value = sum([item[1] * gene for item, gene in zip(items, best_individual)])
    best_weight = sum([item[2] * gene for item, gene in zip(items, best_individual)])
    print("Best individual:", best_individual)
    print("Best value:", best_value)
    print("Best weight:", best_weight)

if __name__ == "__main__":
    genetic_algorithm()
