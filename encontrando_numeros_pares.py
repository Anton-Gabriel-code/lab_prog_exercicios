def achando_pares(lista):
  n_pares = []
  for n in lista:
    if n % 2 == 0:
      n_pares.append(n)
  return n_pares
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
achando_pares(numeros)
