# Program 1 - program that prompts user to enter a string and returns in alphabetical order, a letter and its frequency of occurrence in the string


def count_letters(string):
    string = string.lower()
    letters = {}
    for char in string:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    sorted_letter = sorted(letters.items())
    print("Letter \t frequency: ")
    for letter, frequency in sorted_letter:
        print(f"{letter} \t {frequency}")
def main():
    input_str = input("Enter a string: ")
    count_letters(input_str)
    
if __name__ == '__main__':
    main()