def buscando(lista, n):
  if n in lista:
    print(f"O {n} está presente na lista.")
    return 
  else:
    print(f"O {n} não foi encontrado.")
    return 

x = int(input("Insira o número que deseja buscar: "))
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
buscando(numeros, x)
