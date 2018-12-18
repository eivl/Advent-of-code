from dataclasses import dataclass

with open('day15_input.txt') as f:
    content = f.readlines()

@dataclass
class Unit:
    unit_type: str
    hp: int
    x_pos = int
    y_pos = int

    def move(self):
        pass

    def attack(self):
        pass

    def in_range(self):
        pass

    def reachable(self):
        pass

    def nearest(self):
        pass

    
