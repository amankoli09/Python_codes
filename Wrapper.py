def decorator(func):
    def wrapper():
        func()
        print("This is a decorated function.")
        func()
        print("End of decorated function.")
        func()
    return wrapper

@decorator
def greet():
    print("Hello, World!")  
greet()