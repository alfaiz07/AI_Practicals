# Goal Stack Planning - Blocks World

initial = ['A', 'B', 'C']  # A on table, B on A, C on B
goal = ['C', 'B', 'A']     # C on table, B on C, A on B

def solve():
    print("Initial State:", initial)

    print("\nActions:")
    print("1. Move C to Table")
    print("2. Move B to C")
    print("3. Move A to B")

    print("\nGoal State:", goal)

solve()