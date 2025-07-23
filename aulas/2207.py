notas = [0.0] * 7

while(True):
    for i in range(0, ):
        notas[i] = float(input(f"Nota {i + 1}: "))
        
        if(i == 0):
            maior = notas[i]
            menor = notas[i]
        
        if(notas[i] > maior):
            maior = notas[i]
        if(notas[i] < menor):
            menor = notas[i]

    soma = notas[0] + notas[1] + notas[2] + notas[3] + notas[4] + notas[5] + notas[6] + menor - maior
    media = soma / 5

    print(f"Notas descartas {maior} e {menor}")
    print(f"Média: {media}")

    continuar = input("Continuar? (S/N): ").upper()
    if(continuar != "S"):
        break