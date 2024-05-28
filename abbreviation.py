# Program 8 -  Write a program to read a name and then display it in abbreviated form like, Janak Raj Thareja should be displayed as JRT.

def abbreviate(full_name):
    words = full_name.split()
    abbreviated_name = ""
    for word in words:
        abbreviated_name += word[0].upper()
    return abbreviated_name
    
def main():
    full_name = input("Enter full name: ")
    sort_name = abbreviate(full_name)
    print(f"Abbreviated form of {full_name} is {sort_name}")
    
if __name__ == "__main__":
    main()