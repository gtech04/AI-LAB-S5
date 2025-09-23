from itertools import permutations

def is_valid_assignment(assignment):
    T = assignment['T']
    W = assignment['W']
    O = assignment['O']
    F = assignment['F']
    U = assignment['U']
    R = assignment['R']

    if len(set(assignment.values())) != len(assignment):
        return False
    if F == 0 or T == 0:
        return False

    C10 = (O + O) // 10
    C100 = (W + W + C10) // 10
    C1000 = (T + T + C100) // 10

    if (O + O) % 10 != R:
        return False
    if (W + W + C10) % 10 != U:
        return False
    if (T + T + C100) % 10 != O:
        return False
    if C1000 != F:
        return False

    return True

def local_search():
    letters = ['T', 'W', 'O', 'F', 'U', 'R']
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        if is_valid_assignment(assignment):
            return assignment
    return None

solution = local_search()
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
