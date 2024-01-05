class solution:
    def __init__(self):
        self.name = "mohammad"
        self.age = 18
    def print_following(self):
        print(self.name)
        print(self.age)

obj = solution()
print(vars(obj))
print(dir(obj))