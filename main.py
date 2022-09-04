from Jeux import Jeux
from CodeRayon import CodeRayon

if __name__ == '__main__':
    code_rayon = CodeRayon("FRA.12.42.2021")
    jeu = Jeux("console", "sport", 200, "cool description", code_rayon)

    print(jeu.jeu_is_valide())
