class Jeux:
    def __init__(self, console, genre, prix, description, code_rayon):
        self.console = console
        self.genre = genre
        self.prix = prix
        self.description = description
        self.code_rayon = code_rayon

    def jeu_is_valide(self):
        if not self.code_rayon.code_rayon_isvalide():
            return False
        if not (self.genre == "RPG" or self.genre == "sport" or self.genre == "simulation"):
            return False
        if self.console == "FakeConsole":
            return False
        return True

