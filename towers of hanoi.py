def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move top n-1 disks from source to auxiliary
    towers_of_hanoi(n-1, source, destination, auxiliary)

    # Move the nth disk to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination
    towers_of_hanoi(n-1, auxiliary, source, destination)


# Number of disks
n = int(input("Enter number of disks: "))

print("\nSequence of moves:\n")
towers_of_hanoi(n, 'A', 'B', 'C')
