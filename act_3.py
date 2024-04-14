import csv
''''''
''''''
def stage1():
    print("Stage 1: Load Data")
    while True:
        try:
            file = input("Please enter path to the csv file:")
            csv_data = load_data(file)
            return csv_data
        except FileNotFoundError:
            print("Wrong input. File not found. Please enter a valid path to the csv file.")


def load_data(file):

    try:
        with open(file, 'r') as csvFile:
            csv_reader = csv.reader(csvFile)
            print("File exists.\nLoading file...\nFile successfully loaded!")
            for line in csv_reader:
                print(line)
            return csv_reader
    except FileNotFoundError:
        print("Wrong input. Please enter path to the csv file:/files/sales.csv")


def column():
    print("Choose column from selection below to clear and prepare data:")
    print("Branch / Product / Price / Units sold")
    while True:
        try:
            col = input("Please choose column:")
            if col == "Price" or col == "Units sold":
                return col
            else:
                raise ValueError("Invalid column choice. Please choose a valid column.")
        except ValueError:
            print("It is a non numerical column, choose a numerical one")


def stage2(data):

    print("Stage 2: Clean and prepare data")
    while True:
        try:
            choice = int(input("Would you like to replace empty cells from column with:\n1. Maximum value from column\n2. Minimum value from column\n3. Average value from column\nEnter your choice: "))
            if choice in [1, 2, 3]:
                # Perform data preparation based on choice
                updated_data = prepare_data(data, choice)
                print("All empty values replaced with appropriate values!")
                print("Updated column:")
                print(updated_data)  # Print the updated column
                break
            else:
                print("Invalid choice. Please enter a valid option (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a valid choice (1, 2, or 3).")


def prepare_data(data,choice):
    # Perform data preparation based on choice
    # For now, just return the original data
    return data

def stage3(data):
    print("Stage 3: Analyze data")
    while True:
        try:
            choice = int(input("Please choose if you want to sort column in:\n1. Ascending order\n2. Descending order\nPlease enter your choice: "))
            if choice in [1, 2]:
                sorted_data = sort_column(data, choice)
                print("Column values are sorted accordingly:")
                print(sorted_data)  # Print the sorted column
                break
            else:
                print("Invalid choice. Please enter a valid option (1 or 2).")
        except ValueError:
            print("Invalid input. Please enter a valid choice (1 or 2).")


def sort_column(data,choice):
    # Perform sorting based on choice
    # For now, just return the original data
    return data

def stage4(data):
    print("Stage 4: Visualize Data")
    print("Column: Units sold\nLegend: each '*' represents 5 units")
    units_sold_column = [int(row[3]) for row in data]  # Extracting the 'Units sold' column
    for units_sold in units_sold_column:
        print("" * (units_sold // 5))  # Print '' based on every 5 units sold


def main():
    print("------------------------")
    print("Welcome to Data Analysis CLI")
    print("------------------------")
    print("Program stages:\n1. Load Data\n2. Clean and prepare data\n3. Analyze Data\n4. Visualize Data")
    print()
    csv_data = stage1()
    print(csv_data)  # Print loaded data here
    column_choice = column()
    print("Chosen column: ",column_choice)  # Print chosen column here
    stage2(csv_data)
    stage3(csv_data)
    stage4(csv_data)
    print("Thank you and goodbye!")

if __name__ == "__main__":
    main()