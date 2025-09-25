def fonction1(a,b):
    return list(zip(a,b))

def filter_sup(l):
    return list(filter(lambda p:p[1]>=30,l))

def tansformer(produits):
    r1=[]
    for a in produits :
        produit_finaux= (f"le produit {a[0]} cout {a[1]}DH")  
        r1.append(produit_finaux)
    return r1
def trier(d): 
    return d.sort()