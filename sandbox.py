

class Person:
    def __init__(self):
        print("Instance of Init")
    
    def __call__(self):
        print("Instance of __call__")

p = Person()
p()

