# chat.py
from animal import Animal

class Chat(Animal):
    def parler(self):
        return f"le {self.nom} dit miaw miaw"
