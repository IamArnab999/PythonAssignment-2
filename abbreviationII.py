# Program 9 -  Write a program to read a name and then display it in abbreviated form like janak raj thareja displayed as J.R. Thareja.

def abbreviate(full_name):
    words = full_name.split()
    abbreviated_name = ""
    abbreviated_name += words[0][0].upper()+"."
    for word in words[1:-1]:
        abbreviated_name += word[0].upper()+"."
    abbreviated_name += " " + words[-1].capitalize()
    return abbreviated_name
    
def main():
    full_name = input("Enter full name: ")
    sort_name = abbreviate(full_name)
    print(f"Abbreviated form of {full_name} is {sort_name}")
    
if __name__ == "__main__":
    main()