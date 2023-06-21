# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# PThompson,6.20.2023,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Exceptions / Error Handling--------------------------------------------------------- #
class InvalidChoiceException(Exception):  # custom exception to be used later
    """Raised when input is invalid."""
    pass


class InvalidEntryFormat(Exception):  # custom exception to be used later
    """Raised when input format type is invalid"""
    pass


# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
dic_new_product_row = {}
new_product_name = None  # string
new_product_price = None  # float 00.00
save_status = True  # flag for save status


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
        to_string() returns comma separated product data (alias for __str__())
        display() prints string that object was created
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        PThompson,6.11.2023,Modified code to complete assignment 8
    """

    # pass  # remove after code is added

    # -- Constructor ---
    def __init__(self, name, price=0.00):
        self.product_name = name  # defining the attribute, will be managed by property
        self.product_price = price

    # -- Properties --
    @property
    def product_name(self):
        return str(self.__product_name).title()  # private attribute of product name with formatting

    @product_name.setter
    def product_name(self, value):
        if not str(value).isnumeric():  # exception handling checks to make sure product name is not numeric.
            self.__product_name = value
        else:
            raise Exception("The product name should not be a number.")

    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        if str(value).replace(".", "").isnumeric():  # exception handling checks to make sure the value is a float
            self.__product_price = round(float(value), 2)  # sets property and rounds price to two decimal places
        else:
            raise Exception("The product value should be a number in dollars and cents, e.g. '19.99' ")

    # -- Methods --
    def to_string(self):
        """" Returns a string with the product data """
        return self.__str__()  # creates alias for the __str__ method

    def __str__(self):
        """" Returns a string with the product data """
        return self.product_name + ',' + str(self.product_price)  # returns string csv line with product data

    def display(self):
        print("Item", self.product_name, "with price", self.product_price, "created.")


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        PThompson,6.12.2023,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        try:
            file = open(file_name, "r")  # if file exists, read it and do the following
            for line in file:
                product, price = line.split(",")
                row = {"Product": product.strip(),
                       "Price": price.strip()}  # creates dictionary row from each line in file
                list_of_rows.append(row)  # adds each row to the list
            file.close()
        except FileNotFoundError:  # if file doesn't exist, it creates the file
            file = open(file_name, 'w')
            file.close()
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "w")  # PT opens file with passed in file_name parameter
        for row in list_of_rows:
            file.write(str(row["Product"]) + "," + str(row["Price"]) + "\n")  # saves each row to file
        file.close()
        return list_of_rows


class DataProcessor:
    """Processes entered data into a list to add to file later:

        methods:
            add_data_to_list(list_of_product_objects, new_product_row):

            remove_data_from_list(list_of_product_objects, row_to_remove):

        changelog: (When,Who,What)
            PThompson,6.12.2023,Created Class
        """

    @staticmethod
    def add_data_to_list(list_of_rows, new_product_row):
        """ Adds new data row to existing list of data

        :param list_of_rows: (list) with rows of products and prices:
        :param new_product_row: (dictionary) dictionary row with new product and price to add:
        :return: (list) of dictionary rows
        """
        row = new_product_row
        list_of_rows.append(row)  # appending table with new entries as new dictionary row
        return list_of_rows

# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output

    methods:
        print_menu_items():

        menu_choice():

        print_current_list_items(list_of_rows):

        input_product_data():

        menu_choice():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
        PThompson,6.12.2023,Modified code to complete assignment 8
    """

    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    @staticmethod
    def menu_choice():
        """ Gets the menu choice from a user

        :return: choice (string) menu selection
        """
        choice = None
        valid_choices = ["1", "2", "3", "4"]  # created a list of valid choices for error handling
        while choice not in valid_choices:  # repeats loop until valid option is chosen, else kicks exception
            try:
                choice = input("Choose a menu option: ")
                if choice not in valid_choices:
                    raise InvalidChoiceException
            except InvalidChoiceException:
                print("Invalid option. Please select an option 1 through 4 from the menu.")
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows):
        """ Shows the current products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current list of products is: *******")
        for row in list_of_rows:
            print(row["Product"] + " ($" + str(row["Price"]) + ")")  # prints data rows in desired format
        print("************************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_info():
        """  Gets product and prices values to be added to the list

        :return: (string, float) with product and price
        """
        while (True):
            try:
                print()  # Add an extra line for looks
                product = input("Product name: ").title().strip()  # captures user input and uses strip method
                if str(product).replace(".", "").isnumeric() == True:  # includes replacing . in case there is a price entered
                    raise InvalidEntryFormat
                else:
                    break  # and captures product input
            except InvalidEntryFormat:
                print(" **  A numeric value is not expected for a product name. Please enter again. ** ")

        while (True):
            try:
                price = input("Standard price: (00.00): ").strip()  # captures price and converts to float
                if str(price).replace(".", "").isnumeric() == False:  # exception handling checks to make sure the value is a float
                    raise InvalidEntryFormat
                else:
                    break  # and captures product input
            except InvalidEntryFormat:
                print(" **  A numeric price value in the format e.g. 19.99 is required ** ")
        print()  #  Add an extra line for looks
        return product, price

    @staticmethod
    def input_yes_or_no(question):
        """  Gets choice of yes or no

        :param question: (string) with text for input prompt:
        :return: (string) with save choice
        """
        response = None
        while response not in ("y", "n"):
            response = input(question).lower().strip()
        return response


# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

def main(lstOfProductObjects, strFileName, save_status):
    """ Main body of code
    :param lstOfProductObjects: (list) of product rows
    :param strFileName: (string) of file name
    :param save_Status: (object)

    :return: none
    """
    save_status = save_status
    lstOfProductObjects = FileProcessor.read_data_from_file(file_name=strFileName,
                                                            list_of_rows=lstOfProductObjects)  # reads existing data from file to start
    while (True):
        IO.print_menu_items()  # displays full menu options
        menu_choice_str = IO.menu_choice()  # captures user menu choice and assigns to variable for rest of loop

        if menu_choice_str.strip() == '1':  # choice for showing current data

            IO.print_current_list_items(list_of_rows=lstOfProductObjects)
            continue

        elif menu_choice_str == '2':  # add new item
            new_product_name, new_product_price = IO.input_new_product_info()  # defining new variables with
            obj_new_product = Product(name=new_product_name, price=new_product_price)  # creates new object product
            obj_new_product.display() # prints feedback to user
            # print("New product:", obj_new_product, "added")  # displays feedback to user of product creation (not using)
            dic_new_product_row = {"Product": obj_new_product.product_name,
                                   "Price": obj_new_product.product_price}  # creating new dictionary row from object attributes
            lstOfProductObjects = DataProcessor.add_data_to_list(list_of_rows=lstOfProductObjects,
                                                                 new_product_row=dic_new_product_row)
            save_status = False  # sets flag to false upon addition of new data
            continue
        elif menu_choice_str == '3':  # Save Data to File
            lstOfProductObjects = FileProcessor.write_data_to_file(file_name=strFileName,
                                                                   list_of_rows=lstOfProductObjects)
            print()  # Add an extra line for looks
            print("Data Saved!")
            print()  # Add an extra line for looks
            save_status = True  # sets save status flag to true upon saving data
            continue
        elif menu_choice_str == '4':  # Exit Program
            if save_status == True:  # evaluates if true then breaks and exits
                print()  # Blank line for looks
                print("Goodbye!")
                break
            elif save_status == False:  # evaluates if not saved (false) then prompts for save choice below
                str_save_pick = IO.input_yes_or_no(" ATTENTION: You have unsaved changes."
                                                   " Would you like to save before exiting? (Y or N) ")
                if str_save_pick == "y":
                    lstOfProductObjects = FileProcessor.write_data_to_file(file_name=strFileName,
                                                                           list_of_rows=lstOfProductObjects)
                    print()  # Blank line for looks
                    print("Data Saved!")
                    print()  # Blank line for looks
                    print("Goodbye!")
                    break  # and Exit the program
                elif str_save_pick == "n":
                    print("Goodbye!")
                    break


if __name__ == "__main__":  # if condition statement to run directly
    main(lstOfProductObjects, strFileName, save_status)  # runs main code with arguments of variables
    input("\n\nPress the enter key to exit.")

# Main Body of Script  ---------------------------------------------------- #

