def inverter_str(string):
    print(string)

    string_split = string.split(' ')
    lista_str_invertida = []

    for elemento in string_split:
        str_invertida = ''
        tamanho_str = len(elemento)
        indice = -1

        while indice > -tamanho_str-1:
            str_invertida = str_invertida + elemento[indice]
            indice = indice -1

        lista_str_invertida.append(str_invertida)

    resultado = ''
    for elemento in lista_str_invertida:
        resultado = resultado + ' ' + elemento

    return resultado[1:]

print(inverter_str('OGOL IERATSE AN SURYEK '))
