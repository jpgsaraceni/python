def f(var):
    print(var)
    return var+1


def g():
    return f


var = g()(2)
# é o mesmo que f(2), pois g() retorna f.
