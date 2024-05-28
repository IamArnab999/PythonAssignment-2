# Program 3 - Write a program that prompts the user to enter an alphabet. Print all the words in the list that starts with that alphabet.
def those_words(words, alphabet):
    for  word in words:
        if word.lower().startwith(alphabet.lower()):
            print(word)

def main():
    words = ['Mango', 'Lichi', 'Jackfruit', 'Banana', 'Peach', 'Olive', 'Dates', 'Cherry', 'Grapes', 'Kiwi', 'Lemon']
    alph = input("Enter an alphabet: ")
    those_words(words, alph)
    
if __name__ == '__main__':
    main()