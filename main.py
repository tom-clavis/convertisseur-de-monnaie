from forex_python.converter import CurrencyRates

c = CurrencyRates() 

somme = int(input("Somme à convertir :"))
unitesource = input("type de devise : ").upper()
unitedestinataire = input("En quoi voulez vous le convertir ? : ").upper()

print(unitesource, "a" ,unitedestinataire,somme)
result = c.convert(unitesource,unitedestinataire,somme)

print(result)

