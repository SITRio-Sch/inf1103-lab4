def get_valid_input():
    user_input = input("Enter :")

    if user_input.isdigit() and (int(user_input) >= 0):
        return int(user_input)
    elif user_input.lower() == "quit":
        return user_input.lower()
    else:
        user_input = "Input Error"
        print("Invalid Value")
        return user_input

def process_delivery(current_total, new_value): 
    current_total += new_value
    return(current_total)

def calculate_tax(amount):
    return(10/100 * amount)

def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}\nNumber of Failed/Rejected Entries: {failed_attempts}")

def load_inventory():
    file = open("inventory.txt", "a")
    file.close()

    file = open("inventory.txt", "r")
    lines = file.readlines()
    file.close()

    total = 0
    history = []

    if len(lines) > 0:
        total = int(lines[0].strip())

        index = 1
        while index < len(lines):
            history.append(int(lines[index].strip()))
            index += 1

    return total, history

def save_inventory(total, history):
    file = open("inventory.txt", "w")

    file.write(str(total) + "\n")

    for value in history:
        file.write(str(value) + "\n")

    file.close()


inventory, history = load_inventory()
invalid_entries = 0

while True:
    user_input = get_valid_input()

    if user_input == "Input Error":
        invalid_entries += 1
        continue
    elif user_input == "quit":
        generate_report(inventory, invalid_entries)
        print(f"Tax: {calculate_tax(inventory)}")
        save_inventory(inventory, history)
        break
    else:
        history.append(user_input)
        inventory = process_delivery(inventory, user_input)

        if inventory > 500:
            print("Error! Total inventory exceeds 500 units!")
            break
