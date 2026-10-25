def my_decoratator(func):
    def wrapper():
        n = int(input("Enter the no of times to greet: "))
        for i in range(1,n+1):
            print("Before function called....")
            print("Function called ",i,"Times")
            func()
            print("After Function called....")

    return wrapper

@my_decoratator
def greet():
    print("Hello Greet")

greet()