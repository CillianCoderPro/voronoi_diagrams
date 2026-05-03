class File:
    def __init__(self):
        self.elements = []

    def vide(self):
        return len(self.elements) == 0

    def enfiler(self, element):
        self.elements.append(element)

    def defiler(self):
        if self.vide():
            raise IndexError("Impossible de défiler : la file est vide.")
        return self.elements.pop(0)

    def premier(self):
        if self.vide():
            return None
        return self.elements[0]

    def taille(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)