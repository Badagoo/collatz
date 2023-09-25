import time
from colorama import Fore, Style
import matplotlib.pyplot as plt
import json

delay = 0

plt.xlabel("Calculations")
plt.ylabel("Height")
plt.title("Collatz Conjecture")


def main():
    global x, y
    x = []
    y = []

    while True:
        print(Fore.BLUE + "1. View Iterations")
        print(Fore.GREEN + "2. Create Iteration")
        print(Fore.RED + "3. Delete Iterations")
        print(Fore.YELLOW + "4. Exit")
        print(Style.RESET_ALL)

        choice = int(input("> "))

        if choice == 1:
            view_iteration()
        elif choice == 2:
            create_iteration()
        elif choice == 3:
            delete_iteration()
        elif choice == 4:
            break

def add_iteration():
    try:
        with open("iterations.json", 'r+') as file:
            try:
                iterations = json.load(file)
            except json.decoder.JSONDecodeError:
                iterations = []
    except FileNotFoundError:
        with open("iterations.json", 'w') as file:
            iterations = []

    with open("iterations.json", 'r+') as file:
        try:
            iterations = json.load(file)
        except json.decoder.JSONDecodeError:
                iterations = []
        
        # Determine the iteration number
        iteration_number = len(iterations) + 1
        iteration_name = f"iteration{iteration_number}"
        
        # Create a new dictionary for the iteration
        new_iteration = {iteration_name: [x,y]}
        
        # Append the new iteration to the list
        iterations.append(new_iteration)
        
        # Write the updated data back to the file
        file.seek(0)
        json.dump(iterations, file, indent=4)
        file.truncate()

def create_iteration():
    start = int(input("Enter a number: "))
    calculations = 0

    print(Fore.BLUE + f"{start}")
    while start != 1:
        if start % 2 == 0:
            start = start / 2
            print(Fore.GREEN + f"{start}")
        else:
            start = start * 3 + 1
            print(Fore.RED + f"{start}")
        calculations += 1
        x.append(calculations)
        y.append(start)
        time.sleep(delay)

    print(Fore.BLUE + f"Calculations: {calculations}")
    print(Style.RESET_ALL)
    add_iteration()
    x.clear()
    y.clear()

def view_iteration():
    # print out a list of iterations from the json
    try:
        with open("iterations.json", 'r') as f:
            iterations = json.load(f)
            print(f"There are {len(iterations)} iterations. (Select from 1-{len(iterations)}, or type ALL to view all iterations)")
    except: 
        print("No iterations found")
        return
    choice = input("> ")
    if choice == "ALL":
        for i in range(len(iterations)):
            plt.plot(iterations[i][f"iteration{i+1}"][0], iterations[i][f"iteration{i+1}"][1])
        plt.show()
    else:
        try: plt.plot(iterations[int(choice)-1][f"iteration{choice}"][0], iterations[int(choice)-1][f"iteration{choice}"][1])
        except IndexError:
            print("Out of range.")
            return
        plt.show()
    

def delete_iteration():
    with open("iterations.json", 'w') as f:
        f.write("")
    print("All iterations deleted")

    
main()