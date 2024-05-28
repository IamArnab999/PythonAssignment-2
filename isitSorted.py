# Program 6 - Write a function that accepts three integers and return true if they are sorted otherwise it returns false.

def are_sorted(a, b, c):
    return a <= b <= c
    
def main():
    num = []
    for i in range(3):
        n = int(input(f"Enter three integers{i+1}: "))
        num.append(n)
    if are_sorted(num[0], num[1], num[2]):
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()