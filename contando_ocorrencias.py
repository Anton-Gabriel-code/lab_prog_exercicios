def contador(lista, o):
  contagem = 0
  for item in lista:
    if item == o:
      contagem += 1
  return contagem
x = int(input("Insira o numero da ocorrencia para ver quantas vezes ele apareceu: "))
lista_ocorrencias = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
ocorrencias = contador(lista_ocorrencias, x)
print(f"O número {x} apareceu {ocorrencias} vezes na lista.")
