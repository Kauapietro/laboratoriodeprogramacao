limite = int(input("Digite o limite para cintar os números pares: "))

contagem_pares = 0
for i in range (limite + 1):
    if i % 2 == 0:
       contagem_pares += 1 
print(f" Total de números pares encontrados: {contagem_pares}")