ListaFrutas = ["maçã", "Banana", "manga", "Abacaxi", "laranja"]
print(ListaFrutas)

print("\n")

ListaFrutas.append("Kiwi")
print(ListaFrutas)

print("\n")

ListaFrutas.remove("Banana")
print(ListaFrutas)

print("\n")

if "Abacaxi" in ListaFrutas:
    print("Fruta Abacaxi: está na lista")
else:
    print("Fruta Abacaxi: não está na lista")

tamanho = len(ListaFrutas)
print(tamanho)

print("\n")
print(f"Primeira: {ListaFrutas[0]} | Última: {ListaFrutas[-1]}")
