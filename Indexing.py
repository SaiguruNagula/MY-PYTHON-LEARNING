# indexing = accessing the elemnets of string using [] (indexing operator)
#               [start index:end index :step]  # start index is inclusive and end index is exclusive

credit_no= '1234-5678-9012-3456'

print(credit_no[0:4]) # 1234
print(credit_no[5:9]) # 5678
print(credit_no[10:14]) # 9012
print(credit_no[15:19]) # 3456
print(credit_no[0:19:5]) #1593
print(credit_no[::5]) # 1593
print(credit_no[::-1]) # 6543-2109-8765-4321
print(credit_no[-1]) # 6