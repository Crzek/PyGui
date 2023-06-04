

# funcion normal
def clonador(*obj):
    obj2 = obj
    return obj2, *obj


var1 = None
argumento = "erick"


def test(var, arg):
    var = 1
    argumento = "e"
    return var, argumento


print(test(var1, argumento))
print(var1, argumento)
