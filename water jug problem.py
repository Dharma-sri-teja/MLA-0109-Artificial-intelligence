from collections import deque

def water_jug_problem(capA, capB, target):
    visited = set()
    queue = deque()

    # Starting state: both jugs are empty (0,0)
    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()

        # If target found
        if a == target or b == target:
            print("Solution found:")
            print(a, b)
            return True

        # If already visited, skip
        if (a, b) in visited:
            continue

        visited.add((a, b))
        print("Current:", (a, b))

        # Possible operations
        possible_states = [
            (capA, b),        # Fill jug A
            (a, capB),        # Fill jug B
            (0, b),           # Empty jug A
            (a, 0),           # Empty jug B
            (a - min(a, capB - b), b + min(a, capB - b)),  # Pour A → B
            (a + min(b, capA - a), b - min(b, capA - a))   # Pour B → A
        ]

        for state in possible_states:
            if state not in visited:
                queue.append(state)

    return False


# Example usage:
water_jug_problem(4, 3, 2)
