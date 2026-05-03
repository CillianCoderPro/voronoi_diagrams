class Pile:
    def __init__(self):
        self.elements = []

    def vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if self.vide():
            raise IndexError("Impossible de dépiler : la pile est vide.")
        return self.elements.pop()

    def sommet(self):
        if self.vide():
            return None
        return self.elements[-1]

    def taille(self):
        return len(self.elements)

    def __str__(self):
        return self.elements