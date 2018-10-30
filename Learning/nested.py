numbers = [1, 3, 6]

newNumbers = tuple(map(lambda x: x*2, numbers))

for i in newNumbers:
    print(i)


def multiply(x):
    return (x*x)


def add(x):
    return(x+x)


funcs = [multiply,add]

for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)









