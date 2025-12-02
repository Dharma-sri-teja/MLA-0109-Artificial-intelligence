from heapq import heappush, heappop

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Manhattan distance heuristic
def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                dist += abs(target_x - i) + abs(target_y - j)
    return dist

# Convert list to tuple for storing in visited set
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Find blank space (0) position
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate possible moves
def get_neighbors(state):
    x, y = find_zero(state)
    moves = []
    directions = [(0,1),(0,-1),(1,0),(-1,0)]  # right, left, down, up

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

# A* Search Algorithm
def solve_puzzle(start):
    pq = []
    heappush(pq, (heuristic(start), start, []))
    visited = set()

    while pq:
        cost, state, path = heappop(pq)
        if state == goal_state:
            return path + [state]

        visited.add(to_tuple(state))

        for neighbor in get_neighbors(state):
            if to_tuple(neighbor) not in visited:
                heappush(pq, (len(path) + 1 + heuristic(neighbor), neighbor, path + [state]))

    return None

# Example scrambled state
start_state = [[1, 6, 5],
               [7, 3, 8],
               [4, 2, 0]]   # 0 = empty block (_)

solution = solve_puzzle(start_state)

if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution exists")
