def extrair_nomes(lista):
  return list(lista.keys())

i = {"profissao": "programador", "reality": "MasterChef", "Elefante": "Paquiderme", "Daenerys": "Mãe dos Dragões"}
n = extrair_nomes(i)
print(n)
