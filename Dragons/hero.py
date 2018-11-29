from gameunit import *


class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._health_full = 100
        self._attack = 25
        self._experience = 0
        self.name = name

    def attack(self, target):
        target._health -= self._attack
        print(target._name, target._health, '/', target._health_full, 'HP')

    def exp_gain(self, target):
        self._experience += target._experience

    def is_lvl_up(self):
        return self._experience > 99

    def lvl_up(self):
        self._attack += 100
        self._health = 100

    def exp_down(self):
        self._experience = 0


