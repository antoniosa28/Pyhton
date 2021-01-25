lista = ["cruzeiro","flamengo" , "cruzeiro", "corinthians", "gremio", "palmeiras", "palmeiras", "sao paulo"]

lista2 = list()
for elemento in lista:
    if elemento not in lista2:
        lista2.append(elemento)

print(lista2)