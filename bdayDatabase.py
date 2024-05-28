# Program 2 - Write a program that has a dictionary of your friends name as keys and their birthdays as value. Print the items in the dictionary in a sorted order. Prompt the user to enter a name and check if it is present in the dictionary, If the name does not exist, then ask the user to enter dob. Add the details in the dictionary

def sorted_bday(friends_dict):
    sorted_friends = sorted(friends_dict.items())
    print("Friends and their Birthdays: ")
    print("____________________")
    for friends, birthday in sorted_friends:
        print(f"{friends} : {birthday}")
        
def add_or_update_friend(friends_dict, name, dob):
    friends_dict[name] = dob
    print(f"{name}'s birthday({dob}) added/updated successfully.\n")
    
def main():
    friends_bdays = {
        'Alice' : '01-03-1995',
        'Joe' : '23-11-1997',
        'Charlie' : '12-09-1994'
    }
    
    sorted_bday(friends_bdays)
    name = input("Enter friend's name to check if it's present: ")
    if name in friends_bdays:
        print(f"{name}'s birthday is {friends_bdays[name]}")
    else:
        dob = input(f"{name}'s birthday not found, Please enter the DOB(dd-mm-yyyy format): ")
        add_or_update_friend(friends_bdays, name, dob)
    print("Updated friends and their birthdays:")
    print("____________________")
    sorted_bday(friends_bdays)
    
if __name__ == '__main__':
    main()