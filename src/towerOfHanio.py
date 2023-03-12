def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(pow(2,n)-1)
        tower_of_hanoi(n, 'A', 'B', 'C')
               
main()