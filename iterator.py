name = input("enter your name: ")
it = iter(name)
for i in range(len(name)):
    print(next(it))