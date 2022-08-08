def matrix(diccionario):
    key = []
    value = []
    for clave, valor in diccionario.items():
        key.append(clave)
        value.append(valor)

    print("claves sin ordenar")
    print(key)
    print("valores sin ordenar")
    print(value)

    key.sort()
    value.sort()
    print("claves ordenadas")
    print(key)
    print("valores ordenados")
    print(value)


def run():
    print("obejto tipo diccionario, clave: valor")
    diccionario = {
        'd': 4,
        'f': 6,
        'c': 3,
        'a': 1,
        'g': 7,
        'b': 2,
        'e': 5,
    }
    matrix(diccionario)


if __name__ == '__main__':
    run()
