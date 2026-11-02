import heapq

# Initial state (0 represents the blank space)
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate possible next states
def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_pos] = (
                new_state[new_pos], new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search Algorithm
def a_star(start):
    priority_queue = []

    heapq.heappush(priority_queue, (heuristic(start), 0, start, [start]))

    visited = set()

    while priority_queue:

        f, g, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):

            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None


# Display the solution
solution = a_star(start)

print("A* Search Solution for 8 Puzzle")
print("--------------------------------")

if solution:
    for step, state in enumerate(solution):
        print("\nStep", step)

        for i in range(0, 9, 3):
            print(state[i:i+3])

    print("\nTotal moves:", len(solution) - 1)

else:
    print("No solution found.")