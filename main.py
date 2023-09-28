# Funny numbers to test out with this
# 27, 9663


import time
from colorama import Fore, Style
import matplotlib.pyplot as plt
import json

delay = 0.25 # Delay between each calculation

# Graph Settings
plt.xlabel("Calculations")
plt.ylabel("Height")
plt.title("Collatz Conjecture")

x, y = [], []

def main():
    while True:
        print(Fore.BLUE + "1. View Iterations")
        print(Fore.GREEN + "2. Create Iteration")
        print(Fore.RED + "3. Delete Iterations")
        print(Fore.YELLOW + "4. Exit")
        print(Style.RESET_ALL)

        action = {1: view_iteration, 2: create_iteration, 3: delete_iteration}.get(int(input("> ")), None)
        if action is None:break
        else:action()

def add_iteration():
    try:
        with open("iterations.json", 'r+') as file:
            try: iterations = json.load(file)
            except json.decoder.JSONDecodeError: iterations = []
    except FileNotFoundError:
        with open("iterations.json", 'w') as file: iterations = []

    with open("iterations.json", 'r+') as file:
        try: iterations = json.load(file)
        except json.decoder.JSONDecodeError: iterations = []
        
        iteration_number = len(iterations) + 1
        iteration_name = f"iteration{iteration_number}"
        
        new_iteration = {iteration_name: [x,y]}
        
        iterations.append(new_iteration)
        
        file.seek(0)
        json.dump(iterations, file, indent=4)
        file.truncate()

def create_iteration():
    start = int(input("Enter a number: "))
    calculations = 0

    print(Fore.BLUE + f"{start}")
    while start != 1:
        if start == 0: break
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
    with open("iterations.json", 'w') as f: f.write("")
    print("All iterations deleted")

    
main()