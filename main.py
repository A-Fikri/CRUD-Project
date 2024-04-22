# File to store data
DATA_FILE = "items.txt"

# Function to load items from file
def load_items():
    try:
        with open(DATA_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Function to save items to file
def save_items():
    with open(DATA_FILE, "w") as file:
        for item in items:
            file.write(item + "\n")

# Initialize items with data from file
items = load_items()

def create_item():
    item = input("Enter the item: ")
    items.append(item)
    print("Item added successfully!")

def read_items():
    if not items:
        print("No items found.")
    else:
        print("Items:")
        for index, item in enumerate(items, 1):
            print(f"{index}. {item}")

def update_item():
    read_items()
    index = int(input("Enter the index of the item you want to update: ")) - 1
    if 0 <= index < len(items):
        new_item = input("Enter the new item: ")
        items[index] = new_item
        print("Item updated successfully!")
    else:
        print("Invalid index.")

def delete_item():
    read_items()
    index = int(input("Enter the index of the item you want to delete: ")) - 1
    if 0 <= index < len(items):
        del items[index]
        print("Item deleted successfully!")
    else:
        print("Invalid index.")

def main():
    while True:
        print("\nMenu:")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_item()
        elif choice == "2":
            read_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Exiting...")
            # Save items to file before exiting
            save_items()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
