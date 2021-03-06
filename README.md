# Premier
Premier is a module that allows you to manipulate prime numbers

###### La méthode: prime_and_not ######

Cette méthode retourne des nombres sur un intervalle donné dans une liste en indiquant si ils sont premier ou non.
Elle prend deux paramètres la valeur minimal de l'intervalle et ça valeur maximal. 

Exemple:

  code:
  
    from Premier import Premier
    instance = Premier()
    print(instance.prime_and_not(0, 10))
    
  output:
  
    ["0 n'est pas un nombre premier", "1 n'est pas un nombre premier", '2 est un nombre premier', '3 est un nombre premier', "4 n'est pas un nombre premier:4=2*2", '5 est un nombre premier', "6 n'est pas un nombre premier:6=2*3", '7 est un nombre premier', "8 n'est pas un nombre premier:8=2*4", "9 n'est pas un nombre premier:9=3*3", "10 n'est pas un nombre premier:10=2*5"]
    
###### La méthode: prime ######

Cette méthode retourne l'ensemble des nombres premiers sur un intervalle donner.
Elle prend deux paramètres la valeur minimal de l'intervalle et sa valeur maximal.

Exemple:
  
  code:
  
    from Premier import Premier
    instance = Premier()
    print(instance.prime(0, 50))
    
  output:
  
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
###### La méthode: is_prime #######
  
Cette méthode vérifie si un nombre ou une liste de nombre est première.
Elle ne prend qu'un paramètre, le nombre ou la liste  en question..
  
Exemple:

  code:
  
    from Premier import Premier
    instance = Premier()
    print(instance.is_prime(23))
    print(instance.is_prime(12))
    print(instance.is_prime([2,3,5,7,9,13,23]))
    print(instance.is_prime([1,4,6,8,10]))
    print(instance.is_prime([2,4,9,7,6,13,23,7,14]))
    
  output:
    
    Le nombre 23 est premier !
    Le nombre 12 n'est pas un nombre premier.
    Tout les nombres de cette liste sont premier.
    Aucun des nombres de cette liste  n'est  premier
    Dans cette liste les nombre premier sont aux nombre de 5 soit: [2, 7, 13, 23, 7],contre 4 nombres non premier :[4, 9, 6, 14]

###### La méthode: decompose ######

Cette méthode permet de décomposer en produit de facteur premier un nombre ou les nombres d'des listes.
Elle ne prend qu'un seul paramètre, un nombre ou une liste de nombres.

Exemple:

  code:
  
    from Premier import Premier
    instance = Premier()
    print(instance.decompose(444))
    print(instance.decompose([8,12,10,20]))
    
  output:
    
    [2, 2, 3, 37]
    [[2, 2, 2], [2, 2, 3], [2, 5], [2, 2, 5]]
    
 
