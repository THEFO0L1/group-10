import csv
import re
'''ahmad hisham abolhusain''' ''' '''
''' ''' ''' '''
''' ''' ''' '''
# Function to read data from csv file and populate global dictionary INVENTORY
def read_data(file_path):
    INVENTORY = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')  # Specify tab as delimiter
        next(reader)  # Skip header row
        for row in reader:
            if len(row) == 3:  # Check if row has enough values
                name = row[0]
                quantity = row[1]
                price = row[2]
                INVENTORY[name] = {'price': float(price), 'quantity': int(quantity)}
            else:
                print(f"Ignoring invalid row: {row}")
    return INVENTORY



# Class for individual articles
class Article:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def getName(self):
        return self._name

    def getPrice(self):
        return self._price

    def getQuantity(self):
        return self._quantity

    def setQuantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        return f"Article: {self._name}, Quantity: {self._quantity}, Price: {self._price}"

# Class for shopping cart
class Cart:
    def __init__(self):
        self.list_of_purchased = []

    def addProduct(self, name, quantity):
        if name in INVENTORY:
            available_quantity = min(quantity, INVENTORY[name]['quantity'])
            self.list_of_purchased.append(Article(name, INVENTORY[name]['price'], available_quantity))
            INVENTORY[name]['quantity'] -= available_quantity

    def removeProduct(self, name, quantity):
        for article in self.list_of_purchased:
            if article.getName() == name:
                quantity_to_remove = min(quantity, article.getQuantity())
                article.setQuantity(article.getQuantity() - quantity_to_remove)
                INVENTORY[name]['quantity'] += quantity_to_remove
                if article.getQuantity() == 0:
                    self.list_of_purchased.remove(article)

    def displayCart(self):
        for article in self.list_of_purchased:
            print(article)

    def checkout(self):
        total_bill = 0
        for article in self.list_of_purchased:
            price = article.getPrice()
            quantity = article.getQuantity()
            if quantity >= 3:
                price *= 0.9  # Apply 10% discount for quantity >= 3
            total_bill += price * quantity
        total_bill *= 1.07  # Apply 7% VAT
        return total_bill

# Function to display menu
def menu():
    print("Welcome to the Shopping System!")
    print("1. List")
    print("2. Cart")
    print("3. Add")
    print("4. Remove")
    print("5. Checkout")
    print("6. Exit")

# Function to validate positive integer input
def validate_input(prompt):
    while True:
        user_input = input(prompt)
        if re.match(r'^\d+$', user_input):  # Check if input is a positive integer
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive integer.")

# Main function
def main():
    global INVENTORY
    INVENTORY = read_data("products.csv")
    cart = Cart()
    while True:
        menu()
        choice = input("Please enter your choice: ")
        if choice == "1":
            print("List of Products:")
            for name, details in INVENTORY.items():
                print(f"{name}: Price - ${details['price']}, Quantity - {details['quantity']}")
        elif choice == "2":
            print("Items in Cart:")
            cart.displayCart()
        elif choice == "3":
            name = input("Enter the name of the product to add: ")
            quantity = validate_input("Enter the quantity to add: ")
            cart.addProduct(name, quantity)
        elif choice == "4":
            name = input("Enter the name of the product to remove: ")
            quantity = validate_input("Enter the quantity to remove: ")
            cart.removeProduct(name, quantity)
        elif choice == "5":
            total_bill = cart.checkout()
            print(f"Total bill (including 7% VAT and discounts): ${total_bill:.2f}")
        elif choice == "6":
            print("Thank you for using the Shopping System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()