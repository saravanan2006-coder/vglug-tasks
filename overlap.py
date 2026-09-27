tuple_data = (1, 2, 3, 4, 5),(10,20,70,50),(100,800,400)
largest = tuple_data[0]
for tup in tuple_data:
    if len(tup) > len(largest):
        largest = tup
print("tuple with maximum length:", largest)
print("length of tuple:", len(largest))