# nested loop = loop inside another loop

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to print: ")
for x in range(row):
    for y in range(column):
        print(symbol, end = "")
    print()


