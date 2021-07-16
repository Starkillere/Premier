# -*- coding: utf-8 -*-

"""
    Créateur: Starkiller
    date de création : 14/07/2021
    langage de programation utiliser : Python3 (version:  3.9.2)
    mise à jour : 16/07/2021 18h48

"""
class Premier:

    def __init__(self):
        self.min = 0
        self.max = 0
        self.nombre = 0
        self.liste = []
        self.random_object = ""
        self.boolen =  True

    #Retourne les  nombres premiers et non premiers sur une plage donner
    def prime_and_not(self, min, max):
        self.min, self.max = min, max
        for n in range(self.min, self.max+1):
            if n > 1:
                for x in range(2, n):
                    if n % x == 0:
                        self.liste.append(str(n)+" n'est pas un nombre premier:"+str(n)+'='+str(x)+'*'+str(n//x))
                        break
                else:
                    self.liste.append(str(n)+" est un nombre premier")
            else:
                self.liste.append(str(n)+" n'est pas un nombre premier")
        return self.liste

    #Retourne des nombre premier sur une plage donner
    def retourn_prime(self, min, max):
        self.min, self.max = min, max
        liste_value = []
        for n in range(self.min, self.max + 1):
            if n > 1:
                for i in range(2,n):
                    if (n % i) == 0:
                        break
                else:
                    liste_value.append(n)
        return liste_value
    
    #vérifie si un nombre est premier 
    def is_prime(self, objet):
        self.random_object = objet
        if type(self.random_object) == int or type(self.random_object) == str:
            try:
                self.random_object = int(self.random_object)
            except ValueError:
                return "Vérfictaion impossible !"

            self.nombre = self.random_object
            i = 2
            while i < self.nombre and self.nombre % i != 0:
                i = i + 1
            if i == self.nombre:
                return "Le nombre "+str(self.nombre)+" est premier !"
            else:
                return "Le nombre "+str(self.nombre)+" n'est pas un nombre premier."

        elif type(self.random_object) == list:
        
            '''

            for e in range(len(self.random_object):
                try:
                    self.random_object[e] = int(self.random_object[e])
                except ValueError:
                    print("objet non décomposable!")

            '''
            try: 
               for e in range(len(self.random_object)):
                   self.random_object[e] = int(self.random_object[e])
            except ValueError:
                return "objet non décomposable!"
         
            self.liste = self.random_object
            lst_p, lst_np = [], []
            compteur =  0 
            for e in self.liste:
                i = 2
                e = int(e)
                while i < e and e % i != 0:
                    i = i + 1
                if i == e:
                    compteur += 1
                    lst_p.append(e)
                else:
                    lst_np.append(e)
            if compteur == len(self.liste):
                return "Tout les nombres de cette liste sont premier."
            elif compteur == 0:
                return "Aucun des nombres de cette liste  n'est  premier"
            else:
                return f"Dans cette liste les nombres premier sont aux nombres de {compteur} soit: {lst_p},\n\
    contre {len(self.liste)-compteur} nombres non premier :{lst_np}"

    #Décompose les nombre en leur produits de facteurs premier
    def decompose(self, objet):
        self.random_object = objet
        liste_facteur = []
        if type(self.random_object) == int or type(self.random_object) == str:
            try:
                self.random_object = int(self.random_object)
            except ValueError:
                return "objet non décomposable!"
                
            new_value = self.random_object
            for n in range(2, 10000):
                if n > 1:
                    for i in range(2,n):
                        if (n % i) == 0:
                            break
                    else:
                        while new_value % n == 0:
                            new_value = new_value / n
                            liste_facteur.append(n)
                        if new_value == 1:
                            return liste_facteur

        elif type(self.random_object) == list:

            '''

            for e in range(len(self.random_object):
                try:
                    self.random_object[e] = int(self.random_object[e])
                except ValueError:
                    print("objet non décomposable!")

            '''
            try: 
               for e in range(len(self.random_object)):
                   self.random_object[e] = int(self.random_object[e])
            except ValueError:
                return "objet non décomposable!"
            liste_secondaire = []
            for value in self.random_object:
                for n in range(2, 10000):
                    if n > 1:
                        for i in range(2,n):
                            if (n % i) == 0:
                                break
                        else:
                            while value % n == 0:
                                value = value / n
                                liste_secondaire.append(n)
                if value == 1:
                    liste_facteur.append(liste_secondaire.copy())
                    liste_secondaire.clear()
            return liste_facteur
