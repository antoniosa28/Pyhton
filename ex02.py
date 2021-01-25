 # Ultilizando lambda
converter = lambda celsius:9/5*celsius+32
celsius=int(input("Temperatura em Celsius:"))
fahr=converter(celsius)
print("Temperatura em Fahrnheit :",fahr)