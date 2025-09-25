def fonction1(a,b):
    return list(zip(a,b))

def filter_sup(l):
    return (filter(lambda p: p[1]>=30 ,l))