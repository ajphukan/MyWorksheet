'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
'''
sampleData = list(map(int, input('Sample Data : ').split(',')))
ListData = sampleData
TupledData = tuple(ListData)

print("List : ",ListData)
print("Tuple : ",TupledData)
