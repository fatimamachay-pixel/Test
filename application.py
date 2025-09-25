from Données import produits,prix
from Les_fonctions import fonction1,filter_sup,tansformer,trier
print(tansformer)

print(filter_sup)
print(produits,prix)
association=fonction1(produits,prix)
print(association)
filter_fct=filter_sup(association)

print(filter_fct)
X=tansformer(association)
print(X)
tri=trier(X)
print(tri)