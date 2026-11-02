from collections import deque

# Initial and goal states
start = (0, 0, 0)
goal = (2, 2, 2)

# Generate all possible valid moves
def get_moves(state):
    rods = [[], [], []]

    # Arrange disks on rods
    for disk, rod in enumerate(state):
        rods[rod].append(disk)

    moves = []

    # Move top disk from one rod to another
    for i in range(3):
        if not rods[i]:
            continue

        disk = rods[i][0]

        for j in range(3):
            if i != j:
                if not rods[j] or disk < rods[j][0]:
                    new_state = list(state)
                    new_state[disk] = j
                    moves.append(tuple(new_state))

    return moves


# Breadth First Search
def tower_of_hanoi():
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        # Check goal state
        if state == goal:
            return path

        # Explore next states
        for new_state in get_moves(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None


# Display solution
solution = tower_of_hanoi()

print("Tower of Hanoi using State Space Search")
print("----------------------------------------")

if solution:
    for step, state in enumerate(solution):
        print("Step", step, ":", state)

    print("\nTotal moves:", len(solution) - 1)
else:
    print("No solution found.")