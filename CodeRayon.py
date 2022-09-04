class CodeRayon:
    def __init__(self, code_rayon):
        self.code_rayon = code_rayon

    def code_rayon_isvalide(self):
        code_rayon_list = self.code_rayon.split('.')
        if len(code_rayon_list)<4 or len(code_rayon_list)>4:
            return False
        else:
            letters= code_rayon_list[0]
            numentreprise= code_rayon_list[1]
            numarticles= code_rayon_list[2]
            circulation= code_rayon_list[3]
            if not letters.isalpha() or (len(letters)<3) or (len(letters>3)):
                return False
            if not numentreprise.isnumeric() or (len(numentreprise)<2) or (len(numentreprise)>2):
                return  False
            if not numarticles.isnumeric() or (len(numarticles)<2) or (len(numarticles)>2):
                return False
            if not circulation.isnumeric(0 or int(circulation)>2022):
                return False
        return True
