def main():
    print("---------------------")
    print("1. Add Stock Code")
    print("2. Add Stock Item")
    print("3. Display Stock List")
    print("4. Exit")

    select = input("What is your selection?: ")


def AddStockCode(): #Option 1
    # prompts the user for a stock code
    # add values to others that are already stored
    # No item be priced higher than R1000.00
    print("Add Stock code")

def  SearchCode():
    # To find a specific stock code
    # Recieve a single string parameter (Stock code)
    # As soon as search value is found the process must halt
    # Successful search must return the index (int) of the stock code
    print("Search for code")

def AddStockItem(): #Option 2
    # Adds stock to system
    # Prompts for stock code and num of items to add
    # Must call the SearchCode function
    # Should never have more than 100 items of any stock type
    print("Add stock item")

def DisplayStockList(): #Option 3
    # Displays every stock code with its associated:
    # Price, num of items in stock, and total stock value for each item
    # Display the total value of all stock in system

    print("Display stock list")
    # Stock code, Instock, Price, Stock value
    # AAA, 10, 50, 500
    # BBB, 5, 20.00, 100
    # Total,, 600


main()

