import sys

moneda_sol_peruano = float(sys.argv[1])
moneda_peso_argentino = float(sys.argv[2])
moneda_dolar_americano = float(sys.argv[3])
peso_chileno = int(sys.argv[4])

conversion = {
  "Sol" : moneda_sol_peruano,
  "Peso_Argentino": moneda_peso_argentino,
  "Dolar_Americano": moneda_dolar_americano
}

conversion_sol = conversion['Sol'] * peso_chileno
conversion_peso_argentino = conversion['Peso_Argentino'] * peso_chileno
conversion_dolar_americano = conversion['Dolar_Americano'] * peso_chileno

print(f"Los {peso_chileno} pesos equivalen a: ")
print(f"{conversion_sol} Soles")
print(f"{conversion_peso_argentino} Pesos Argentinos")
print(f"{conversion_dolar_americano} Dólares")

