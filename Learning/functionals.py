from functools import partial


def mnozenie(x,y,z):
    return (x*y)+z


podwojenie = partial(mnozenie,2,1)

print(podwojenie(6))


