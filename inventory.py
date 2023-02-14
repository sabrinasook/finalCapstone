#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Function to return cost of shoe
    def get_cost(self):
        print(f'Cost = {self.cost}rs')

    # Function to return quantity of shoe stock
    def get_quantity(self):
        print(f'Quantity = {self.quantity}')

    # Function to return class info in str format
    def __str__(self):
        print(f'{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}')


#=============Shoe list===========
# List to store Shoe objects
shoe_list = []

#==========Functions outside the class==============
# Function to read from inventory file and add to shoe list
def read_shoes_data():
    # Read from inventory text file
    # Append each item to list as object in Shoe class
    inventory = open('inventory.txt', 'r')
    inventory_read = inventory.readlines()
    for line in inventory_read:
        line = line.strip('\n').split(',')
        if line[0] != 'Country':
            try:
                line = Shoe(line[0], line[1], line[2], line[3], line[4])
                shoe_list.append(line)
            except IndexError:
                pass
    inventory.close()

# Function to capture new shoe data and append to shoe list
def capture_shoes():
    print('For the new shoe you want to register;')
    new_country = input('Enter the country: ')
    new_code = input('Enter the code: ')
    new_product = input('Enter the product name: ')
    new_cost = input('Enter the cost: ')
    new_quantity = input('Enter the quantity of stock: ')
    # Take data from user input and create object of class Shoe
    # Append Shoe object to list
    new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
    shoe_list.append(new_shoe)
    print(f'New shoe data added.')

# Function to print each item from shoe list in str format
def view_all():
    print('ALl shoes in inventory (country, code, product, cost, quantity):')
    for item in shoe_list:
        try:
            print(item)
        except TypeError:
            pass

# Function to search for item with lowest quantity
# Option to add to quantity and update on file
def re_stock():
    # Sort stock in ascending order
    stock_list = []
    inventory_file = open('inventory.txt', 'r')
    file_read = inventory_file.readlines()
    for line in file_read:
        line = line.strip('\n').split(',')
        if line[0] != 'Country':
            try:
                stock_list.append(int(line[4]))
            except IndexError:
                pass
    stock_list.sort()
    inventory_file.close()

    inventory_file = open('inventory.txt', 'w')
    for line in file_read:
        line = line.strip('\n').split(',')
        try:
            # Find product with lowest stock in list
            line[4] = int(line[4])
            if line[4] == stock_list[0]:
                print(f'Lowest stock is of shoe code {line[1]}, quantity = {line[4]}')
                # Give option to update stock
                update = input('Would you like to update the quantity of stock - yes/no: ')
                if update == 'yes':
                    new_stock = input('Enter the new stock value: ')
                    line[4] = new_stock
                else:
                    pass
            else:
                pass
        except ValueError:
            pass
        # Re-write file with updated stock
        inventory_file.write(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}\n')
    print('File updated.')
    inventory_file.close()

# Function to allow user to view shoe data when searching by code
def search_shoe():
    # Allow user input of shoe code
    search_code = input('Enter the code you would like to search: ').strip(' ')
    found = False
    for item in shoe_list:
        item.code = item.code.strip(' ')
        # If code matches code of shoe in inventory, return details
        if item.code == search_code:
            found = True
            try:
                print(item)
            except TypeError:
                pass
        else:
            pass
    # If code does not match any shoe in inventory, return error message
    if found == False:
        print('Item not found in inventory.')

# Function to return value (cost * quantity) of each shoe in inventory
def value_per_item():
    for item in shoe_list:
        value = int(item.cost) * int(item.quantity)
        print(f'{item.product} (code {item.code}); Value {value}rs')

# Function to return shoe with highest quantity of stock to list as available for sale
def highest_qty():
    # Create list of quantity values
    stock_list = []
    inventory_file = open('inventory.txt', 'r')
    file_read = inventory_file.readlines()
    for line in file_read:
        line = line.strip('\n').split(',')
        if line[0] != 'Country':
            try:
                stock_list.append(int(line[4]))
            except IndexError:
                pass
    stock_list.sort()
    inventory_file.close()

    for item in shoe_list:
        # Match highest stock quantity with shoe object from inventory
        # Display details of this shoe
        if int(item.quantity) == int(stock_list[-1]):
            print(f'{item.product} (code {item.code}) - highest quantity available, for sale')

#==========Main Menu=============
menu_count = 0
while True:
    menu = input('''\nPlease enter an option from the menu: 
c - Capture data about a shoe
va - View details of all shoes in inventory
rs - Check shoes with lowest quantity for re-stocking
s - Search for a shoe by code
v - Check value for each item in inventory
hq - Check product with highest quantity (for sale)
e - Exit
: ''').strip(' ').lower()
    menu_count += 1
    if menu_count == 1:
        read_shoes_data()
    else:
        pass
    if menu == 'c':
        capture_shoes()
    elif menu == 'va':
        view_all()
    elif menu == 'rs':
        re_stock()
    elif menu == 's':
        search_shoe()
    elif menu == 'v':
        value_per_item()
    elif menu == 'hq':
        highest_qty()
    elif menu == 'e':
        print('Goodbye!')
        exit()
    else:
        print('\nInvalid option entered.\nPlease enter an option from the menu.')


