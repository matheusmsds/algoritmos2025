arquivo = open("notas.txt", "r", encoding="utf8")

linhas = arquivo.readlines()

media = 0
for i in range(0, len(linhas)):
    a = linhas[i].split(",")
    if(a[1]):
        a[1] = float(a[1])
    if(i == 0):
        menor_nota = a[1]
        maior_nota = a[1]
        n_menornota = a[0]
        n_maiornota = a[0]
    if(a[1] > maior_nota):
        maior_nota = a[1]
        n_maiornota = a[0]
    if(a[1] < menor_nota):
        menor_nota = a[1]
        n_menornota = a[0]
    media += a[1] / len(linhas)

print(f"Maior Nota\nNome:{n_maiornota}\nNota: {maior_nota}")
print("\n--------\n")
print(f"Menor Nota\nNome:{n_menornota}\nNota: {menor_nota}")
print("\n--------\n")
print("Média Notas")
print(f"média: {media:.2f}")
arquivo.close()