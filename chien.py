# chien.py
from animal import Animal

class Chien(Animal):
    def parler(self):
        return f"le {self.nom} dit how how"
