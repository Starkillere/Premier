# Premier
Premier is a module that allows you to manipulate prime numbers

###### La méthode: retourne_nb_and_pp_D ######

Cette méthode retourne des nombres sur un intervalle donner dans une liste en indiquant si ils sont premier ou non.
Elle prend deux paramètres la valeur minimal de l'intervalle et ça valeur maximal. 

Exemple:

  code:
  
    from Premier import Premier
    instance = Premier()
    print(instance.retourne_nb_p_and_pp_D(0, 50))
    
  output:
  
    ['0 est un nombre premier', '1 est un nombre premier', '2 est un nombre premier', '3 est un nombre premier', '4=2*2', '5 est un nombre premier', '6=2*3', '7 est un nombre      premier', '8=2*4', '9=3*3', '10=2*5', '11 est un nombre premier', '12=2*6', '13 est un nombre premier', '14=2*7', '15=3*5', '16=2*8', '17 est un nombre premier', '18=2*9', '19 est un nombre premier', '20=2*10', '21=3*7', '22=2*11', '23 est un nombre premier', '24=2*12', '25=5*5', '26=2*13', '27=3*9', '28=2*14', '29 est un nombre premier', '30=2*15', '31 est un nombre premier', '32=2*16', '33=3*11', '34=2*17', '35=5*7', '36=2*18', '37 est un nombre premier', '38=2*19', '39=3*13', '40=2*20', '41 est un nombre premier', '42=2*21', '43 est un nombre premier', '44=2*22', '45=3*15', '46=2*23', '47 est un nombre premier', '48=2*24', '49=7*7', '50=2*25']
    
###### La méthode: retourne_nb_p ######

Cette méthode retourne l'ensemble des nombre premier sur un intervalle donner.
Elle prend deux paramètres la valeur minimal de l'intevalle et ça valeur maximal.

Exemple:
  
  code:
  
    from Premier import Premier
    instance = Premier()
    print(instance.retourne_nb_p(0, 50))
    
  output:
  
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
###### La méthode: Verifier_si_nb_premier #######
  
Cette méthode vérifie si un nombre est premier.
Elle ne prend qu'un paramètre, le nombre en question .
  
Exemple:

  code:
  
    from Premier import Premier
    instance = Premier()
    print(instance.Verifier_si_nb_premier(23))
    print(instance.Verifier_si_nb_premier(12))
    
  output:
    
    Le nombre 23 est premier !
    Le nombre 12 n'est pas un nombre premier.
    
###### La méthode: Verifier_si_lst_nb_p ######

Cette méthode vérifie si une liste  est premier.
Elle ne prend qu'un paramètre, la liste en question .

Exemple:

  code:
  
    from Premier import Premier
    instance = Premier()
    print(instance.Verifier_si_lst_nb_p([2,3,5,7,9,13,23]))
    print(instance.Verifier_si_lst_nb_p([1,4,6,8,10]))
    print(instance.Verifier_si_lst_nb_p([2,4,9,7,6,13,23,7,14]))
    
  output:
    
    Tout les nombres de cette liste sont premier.
    Aucun des nombres de cette liste  n'est  premier
    Dans cette liste les nombre premier sont aux nombre de 5 soit: [2, 7, 13, 23, 7],contre 4 nombres non premier :[4, 9, 6, 14]

###### La méthode: decompose ######

Cette méthode permet de décomposer en produit de vacteur premier un nombre ou les nombres d'une liste.
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
    
 
