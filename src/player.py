# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player:
    def __init__(self, name, current_room, inventory=[], item_name=None, item_description=None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __repr__(self):
        return f"{self.name}, you are in the {self.current_room} and carrying these items:\n{self.inventory}"
