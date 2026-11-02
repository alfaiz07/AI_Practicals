from collections import deque

# 0 = Free path, 1 = Obstacle
grid = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

def bfs():
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < 4 and 0 <= ny < 4 and
                grid[nx][ny] == 0 and (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

path = bfs()

if path:
    print("Robot Path:", path)
    print("Total Steps:", len(path) - 1)
else:
    print("No path found")