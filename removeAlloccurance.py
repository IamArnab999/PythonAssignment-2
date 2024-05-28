# Program 7 - Write a program that removes all the occurrences of a specified character from a given string.

def remove_char(input_str, charto_remove):
    modified_str = input_str.replace(charto_remove, "")
    return modified_str

def main():
    input_str = input("Enter a string: ")
    charto_remove = input("Which char you want to remove: ")
    
    modified_str = remove_char(input_str, charto_remove)
    print(f"The modified string after removing {charto_remove}: ")
    print(modified_str)
    
if __name__ == "__main__":
    main()