# se importa el archivo que se leera
with open ('lorem_ipsum.txt', "r") as file:
  lorem_ipsum=file.read()

caracteres = len(set(lorem_ipsum))
palabras = len(set(lorem_ipsum.split()))

print("El número de caracteres distintos es: ", caracteres)
print("El número de palabras distintas es: ", palabras)
