# Program 5 - Write a program to print the Fibonacci series using recursion.

def fibonacci(x):
    if x <= 0:
        return[]
    elif x == 1:
        return[0]
    elif x == 2:
        return[0, 1]
    else:
        fib_series = fibonacci(x-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
    
def main():
    n = int(input("Enter number of terms in the Fibonacci series: "))
    fib_series = fibonacci(n)
    print("Fibonacci series: ")
    for num in fib_series:
        print(num, end=" ")

if __name__ == '__main__':
    main()