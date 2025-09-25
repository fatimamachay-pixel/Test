from Données import produits,prix
from Les_fonctions import fonction1,filter_sup,tansformer,trier,convertir,plus_cher, moins_cher, mention


print(filter_sup)
print(produits,prix)
association=fonction1(produits,prix)
print(association)
filter_fct=filter_sup(association)

print(filter_fct)
X=tansformer(association)
print("X",X)


tri=trier(prix)
print(tri)

convertir_tuple=convertir(tri)
print(convertir_tuple)
prix_plus_cher=plus_cher(convertir_tuple)
print(prix_plus_cher)
prix_moins_cher_reste=moins_cher(convertir_tuple)
print(prix_moins_cher_reste)

mention(association)
