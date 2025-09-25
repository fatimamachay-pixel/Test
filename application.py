from Données import produits,prix
from Les_fonctions import fonction1,filter_sup
print(filter_sup)
print(produits,prix)
association=fonction1(produits,prix)
print(association)
# #filtred :
# filter_sup_30=list(filter_sup(association))
# print(filter_sup_30)

filter_fct=filter_sup(association)
print(filter_fct)
