# Program 10 - Write a program to count the number of digits , upper case character ,lower case character and special characters in a given string.

def count_characters(input_str):
    digi_count = 0
    upp_count = 0
    low_count = 0
    special_count = 0
    for char in input_str:
        if char.isdigit():
            digi_count += 1
        elif char.isupper():
            upp_count += 1
        elif char.islower():
            low_count += 1
        elif not char.isspace():
            special_count += 1
    return digi_count, upp_count, low_count, special_count
    
def main():
    input_str = input("Enter a string: ")
    digi_count, upp_count, low_count, special_count = count_characters(input_str)
    print(f"Number of digits: {digi_count}")
    print(f"Number of upper case characters: {upp_count}")
    print(f"Number of lower case characters: {low_count}")
    print(f"Number of special characters: {special_count}")
    
if __name__ == "__main__":
    main()