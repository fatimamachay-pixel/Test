from Données import produits,prix
from Les_fonctions import resultat
print(produits,prix)
print(resultat)
#association chaque produit à son prix :
resultat=zip(produits,prix)
print(list(resultat))