def fibonacci_iterative(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
def main():

    n = int(input("\nEnter the term n for Fibonacci series: "))

    if n <= 0:
        print("Plese enter a positive integer")

    else:

        print("\nIterative Fibonacci sequence:",end=" ")
        for i in range(n):
            print(fibonacci_iterative(i),end=" ")

        print("\n\nRecursive Fibonacci sequence:",end=" ")
        for i in range(n):
            print(fibonacci_recursive(i),end=" ")
    print("\n")

main()