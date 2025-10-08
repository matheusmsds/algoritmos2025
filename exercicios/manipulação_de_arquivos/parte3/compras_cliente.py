arquivo = open("compras_clientes.txt", "r", encoding="utf8")

linhas = arquivo.readlines()

nome = input("Informe o nome do cliente: ").strip()

total = 0
for i in range(0, len(linhas)):
    a = linhas[i].split(",")
    if(a[1]):
        a[1] = float(a[1])
    
    if(a[0] == nome):
        total += a[1]
        
print(f"{nome} - Total: R${total:.2f}")

arquivo.close()