fruit=["apple","banana","cherry"]
vegetable=["potato","onion","tomato"]
dairy=["milk","curd","paneer"]

grocries=[fruit,vegetable,dairy]
print(grocries) # [['apple', 'banana', 'cherry'], ['potato', 'onion', 'tomato'], ['milk', 'curd', 'paneer']]

print(grocries[0]) # ['apple', 'banana', 'cherry']
print(grocries[1]) # ['potato', 'onion', 'tomato']
print(grocries[1][2])

# use nested loops to print all the items in the list
for i in range(len(grocries)):
    for j in range(len(grocries[i])):
        print(grocries[i][j], end=" ")
    print() # apple banana cherry potato onion tomato milk curd paneer

for k in grocries:
    for l in k:
        print(l) # apple, banana, cherry, potato, onion, tomato, milk, curd, paneer


num_pad = [[1,2,3],[4,5,6],[7,8,9],["#",0,"*"]]

for no in num_pad:
    for n in no:
        print(n, end=" ")
    print() # 1 2 3 4 5 6 7 8 9 # 0 *