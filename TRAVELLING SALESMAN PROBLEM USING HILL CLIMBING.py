import random

def calculate_tour_length(tour, distance_matrix):
    length = 0
    for i in range(len(tour)):
        length += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return length

def generate_neighbor(tour):
    neighbor = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def hill_climbing_tsp(distance_matrix, iterations=1000):
    num_cities = len(distance_matrix)
    current_tour = list(range(num_cities))
    random.shuffle(current_tour)
    current_length = calculate_tour_length(current_tour, distance_matrix)
    for _ in range(iterations):
        neighbor = generate_neighbor(current_tour)
        neighbor_length = calculate_tour_length(neighbor, distance_matrix)
        if neighbor_length < current_length:
            current_tour = neighbor
            current_length = neighbor_length
    return current_tour, current_length

if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    best_tour, best_length = hill_climbing_tsp(distance_matrix)
    best_tour_with_return = best_tour + [best_tour[0]]
    print("Best tour:", best_tour_with_return)
    print("Total distance:", best_length)
