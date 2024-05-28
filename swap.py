# Program 4 - Write a program to swap two variables that are defined as global variable

global_var1 = "Hello"
global_var2 = "World"

def swap_global():
    global global_var1, global_var2
    global_var1, global_var2 = global_var2, global_var1
    
def main():
    print(f"Before swapping: global_var1 = {global_var1}, global_var2 = {global_var2}")
    swap_global()
    print(f"Before swapping: global_var1 = {global_var1}, global_var2 = {global_var2}")
    
if __name__ == "__main__":
    main()