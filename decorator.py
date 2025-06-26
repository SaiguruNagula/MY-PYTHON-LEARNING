#decorator = a function that executes the behaviour of another funcion
#            w/o modifies the base of the fn
#            pass the name of the function as the argument to the decorator

def sprinkler(func):
    def wrapper():
        func()
        print("with added sprinkler")
    return wrapper

@sprinkler
def get_ice_cream():
    print(f"you got ice cream")


get_ice_cream()


