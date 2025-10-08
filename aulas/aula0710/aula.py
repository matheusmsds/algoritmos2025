arq = open("aula.txt", "r")

counteudo = arq.readlines()

soma = 0
for i in range(0, len(counteudo)):
    soma += int(counteudo[i].strip())

print(f"Soma: {soma}")
arq.close()