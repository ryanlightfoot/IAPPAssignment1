
stockCodes = ["ABC"]
stockPrices = [100.00]
count = [4]

def main():

    flag = True

    while(flag):
        print("---------------------")
        print("1. Add Stock Code")
        print("2. Add Stock Item")
        print("3. Display Stock List")
        print("4. Exit")

        select = input("What is your selection?: ")

        if(select == "1"):
            AddStockCode()
        elif(select == "2"):
            AddStockItem()
        elif(select == "3"):
            DisplayStockList()
        elif(select == "4"):
            flag = False
            return
        else:
            print("you need to select from the options...")


def AddStockCode(): #Option 1
    # prompts the user for a stock code
    # add values to others that are already stored
    # No item be priced higher than R1000.00

    stockCode = input("What is the stock code? ")

    stockPrice = float(input("What is the stock price? "))
    while(int(stockPrice) > 1000):
        print("Stock price cannot be above R1000.")
        stockPrice = float(input("What is the stock price? "))

    if stockCode in stockCodes:
        i = SearchCode(stockCode)
        stockPrices[i] = stockPrice # Update to new stock price
        count[i] = 0 # creates amount of stock
    else:
        stockCodes.append(stockCode) # Create new stock
        stockPrices.append(stockPrice)
        count.append(0)

def SearchCode(stockCode):
    # To find a specific stock code
    # Recieve a single string parameter (Stock code)
    # Successful search must return the index (int) of the stock code
    if stockCode in stockCodes:
        return stockCodes.index(stockCode)
    else:
        print("Stock was not found")
        return -1

def AddStockItem(): #Option 2
    # Adds stock to system
    # Prompts for stock code and num of items to add
    # Must call the SearchCode function
    # Should never have more than 100 items of any stock type
    stockCodeAdd = input("What is the stock code? ")

    i = SearchCode(stockCodeAdd)
    if i == -1:
        return

    amtStockAdd = int(input("How much stock do you want to add? "))

    if((int(count[i]) + amtStockAdd) <= 100):
        count[i] += amtStockAdd
        return
    else:
        print("Cannot be more than 100 items of stock")



def DisplayStockList(): #Option 3
    # Displays every stock code with its associated:
    # Price, num of items in stock, and total stock value for each item
    # Display the total value of all stock in system

    print("Stock code, In stock, Price, Stock value")
    txt = "{0},\t{1},\t{2},\t{3}"
    tot = 0.0

    for i in range(len(stockCodes)):
        stk_val = float(stockPrices[i]) * float(count[i])
        print(txt.format(stockCodes[i], count[i], stockPrices[i], stk_val))
        tot = tot + stk_val
    print("Total\t,\t,\t" + str(tot))
    # Stock code, Instock, Price, Stock value
    # AAA, 10, 50, 500
    # BBB, 5, 20.00, 100
    # Total,, 600


main()

