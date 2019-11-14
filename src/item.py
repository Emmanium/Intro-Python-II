class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have picked up {self.name}')

    def __repr__(self):
        return (f'Name: {self.name}, Description: {self.description}')
