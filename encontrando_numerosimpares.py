def achando_impares(lista):
  n_impares = []
  for n in lista:
    if n % 2 != 0:
      n_impares.append(n)
  return n_impares
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
achando_impares(numeros)
