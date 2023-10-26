class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print(f"breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("swimming")
    
    def breathe(self):
        super().breathe()
        print('makes bubbles')


nemo = Fish()
nemo.swim()
nemo.breathe()