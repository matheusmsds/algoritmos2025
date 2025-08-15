import random
# 2) Crie uma função para pedir um número inteiro ao usuário e retornar ele. 
# Toda vez que você precisar de um número informado pelo usuário, utilize ela. 
# Ela não tem parâmetro e o retorno é o valor digitado pelo usuário já com o tipo inteiro.
def InputInt(msg:str):
    while (True):
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Entrada Inválida. Por favor digite um número inteiro.")

# 3) Faça uma função para gerar números aleatórios. Esta 
# função deve receber um número inteiro por parâmetro e retornar um número aleatório entre 1 e ele. Assim, 
# toda vez que você precisar de um número qualquer pode usar a função do exercício 1 ou esta.
def GerarNumero(numero: int):
    n = random.randint(1, numero)
    return n

# 4) Crie duas funções para sortear números aleatórios. As
# funções devem receber o limite inferior e o superior por parâmetros. 
# Uma função deve retornar um número par e a outra um número ímpar. Detalhe: uma função não pode ser criada dentro de outra.
def sortear_par(limite_inferior, limite_superior):
    tamanho = (limite_superior - limite_inferior + 1)
    array = [0] * tamanho  #
    indice = 0

    for num in range(limite_inferior, limite_superior + 1):
        if(num % 2 == 0):
            array[indice] = num
            indice += 1

    if(indice == 0):
        raise ValueError("Não há números pares no intervalo fornecido.")

    sorteado = array[random.randint(0, indice - 1)]
    return sorteado


def sortear_impar(limite_inferior, limite_superior):
    tamanho = (limite_superior - limite_inferior + 1)
    array = [0] * tamanho  
    indice = 0

    for num in range(limite_inferior, limite_superior + 1):
        if(num % 2 != 0):
            array[indice] = num
            indice += 1

    if(indice == 0):
        raise ValueError("Não há números ímpares no intervalo fornecido.")

    sorteado = array[random.randint(0, indice - 1)]
    return sorteado

# 5) Faça uma função que receba um número inteiro por parâmetro e retorne o mês correspondente ao número. 
# Por exemplo, 2 corresponde a "Fevereiro". Se o número informado não corresponder a um mês (1 a 12), 
# retorne a mensagem “Mês inválido”.
def retornar_mesInteiro(n: int):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if(1 <= n and n <= 12):
        return meses[n - 1]
    else:
        return "Mês Inválido"
# 6) Faça funções para resolver as equações de área:
# a) do quadrado = x² 
def area_quarado(x: int):
    return x ** 2
# b) do retângulo = b . h 	(base x altura)
def area_retangulo(b: int, h:int):
    return b * h
# c) do triângulo= (b . h)2
def area_trinagulo(b: int, h:int):
    return (b * h) / 2
# d ) do trapézio = (B + b) . h2
def area_trapézio(B:int, b: int, h:int):
    return ((B + b) * h) / 2

# 7) Faça um programa para calcular o Fatorial de um número. 
def fatorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * fatorial(n - 1)
# 8) Faça uma função que receba um vetor como parâmetro e retorne apenas o maior valor deste vetor.
def Maiorvalor_vetor(vetor):
    for i in range(0, len(vetor)):
        if(i == 0):
            maior = vetor[i]
        if(vetor[i] > maior):
            maior = vetor[i]
    return maior
# 9( Faça uma função que receba um vetor como parâmetro e retorne apenas o menor valor deste vetor.
def Menorvalor_vetor(vetor):
    for i in range(0, len(vetor)):
        if(i == 0):
            menor = vetor[i]
        if(vetor[i] < menor):
            menor = vetor[i]
    return menor

# 10) Faça uma função para receber um vetor como parâmetro, calcular a soma desse vetor e retornar apenas a média dos valores.
def Media_vetor(vetor):
    soma = 0
    for i in range(0, len(vetor)):
        soma += vetor[i]
    return soma / len(vetor)

# 11) Faça uma função que recebe um vetor de números inteiros como parâmetro. 
# Esta função deve calcular o dobro de cada valor do vetor e retornar um vetor inteiro atualizado com o dobro de cada número. 
# Dica: crie outro vetor dentro da função com o mesmo tamanho para preencher com o dobro. 
def dobro_vetor(vetor):
    dobro_vetor = [0] * len(vetor)
    for i in range(0, len(vetor)):
        dobro_vetor[i] = vetor[i] * 2
    return dobro_vetor


# 12) Construa uma função que receba por parâmetro uma data no formato DD/MM/AAAA e devolva uma string no formato DD de Mês Por Extenso de AAAA. Para pegar o mês por extenso, utilize a função criada no exercício 3. Por exemplo: 18/09/2019 retorna 18 de Setembro de 2019.

def data_por_extenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    try:
        partes = data.split("/")
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        if(1 <= mes and mes <= 12):
            nome_mes = meses[mes - 1]
            return f"{dia:02d} de {nome_mes} de {ano}"
        else:
            return "Mẽs Inválido."
    except ValueError:
        return "Data em formato inválido."

# 13) Faça uma função que retorne o reverso de um número inteiro informado por parâmetro. Por exemplo: 127 retorna 721.
def numero_reverso(numero):
    string = str(numero)
    invertida = ""
    for i in range(len(string) -1, -1, -1):
        invertida += string[i]
    return int(invertida)

# 14) Faça uma função que recebe uma frase (ou palavra) por parâmetro e retorne essa frase invertida. Por exemplo: Rafael retorna leafaR
def string_reversa(string):
    invertida = ""
    for i in range(len(string) -1, -1, -1):
        invertida += string[i]
    return invertida

# 15) Faça uma função que recebe uma frase (ou palavra) por parâmetro e retorne quantas vogais essa frase tem. Por exemplo: se a frase for “Rafael” a função retorna 3

def contar_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    contador = 0

    for letra in string:
        for v in vogais:
            if letra == v:
                contador += 1
    return contador

# 16) Construa uma função que receba uma string como parâmetro e retorne outra string com os caracteres embaralhados. 
# Por exemplo: se a função receber a palavra “Python”, pode retornar “npthyo”, “ophtyn” ou qualquer outra combinação possível, 
# de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, 
# independentemente de como foram digitados.

def embaralhar_frase(string):
    string = string.lower()
    tamanho = len(string)
    array_chars = [''] * tamanho
    
    for i in range(0, tamanho):
        array_chars[i] = string[i]
    
    for i in range(0, tamanho):
        j = random.randint(0, tamanho - 1)
        temp = array_chars[i]
        
        array_chars[i] = array_chars[j]
        array_chars[j] = temp
    
    string_formatada = ""
    for i in range(0, tamanho):
        string_formatada += array_chars[i]
        
    return string_formatada

# 17) Refaça o exercício anterior, porém sem repetir os caracteres. Exemplo: com a string “Python” 
# não se pode ter como retorno “nhtohpy” com caracteres repetidos (a não ser que a palavra contenha 
# caracteres repetidos, como Rafael).
def embaralhar_sem_repetir(texto):
    texto = texto.lower()
    
    # Cria uma lista com os caracteres da string
    tamanho = len(texto)
    origem = [''] * tamanho
    for i in range(tamanho):
        origem[i] = texto[i]

    # Lista auxiliar para controlar o que já foi usado
    usados = [False] * tamanho
    resultado_array = [''] * tamanho
    pos_resultado = 0

    while (pos_resultado < tamanho):
        # Escolhe um índice aleatório
        indice = random.randint(0, tamanho - 1)

        if (not usados[indice]):
            # Conta quantas vezes o caractere já foi usado no resultado
            letra = origem[indice]
            repete = 0
            for j in range(pos_resultado):
                if resultado_array[j] == letra:
                    repete += 1

            # Conta quantas vezes ele aparece no original
            total = 0
            for j in range(tamanho):
                if origem[j] == letra:
                    total += 1

            # Só adiciona se não passou do número de ocorrências no original
            if(repete < total):
                resultado_array[pos_resultado] = letra
                pos_resultado += 1
                usados[indice] = True

    # Junta os caracteres numa string final
    resultado = ''
    for i in range(tamanho):
        resultado += resultado_array[i]

    return resultado

# 18) Crie uma função para gerar senhas aleatórias com letras, 
# números e caracteres especiais. A função deve receber o tamanho da senha 
# (quantidade de caracteres) e retornar uma senha aleatória com esse tamanho 
# podendo conter letras minúsculas, maiúsculas, números ou caracteres especiais (!@#$%&*()-+[{]}?). Por exemplo: se o tamanho for 8 a função deve retornar uma senha com 8 caracteres, como: a8B&Om1j.
def gerar_senha(tamanho):
    if tamanho <= 0:
        return ''

    # Caracteres possíveis
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    especiais = '!@#$%&*()-+[{]}?'

    # Junta todos os caracteres em um array
    todos = letras_maiusculas + letras_minusculas + numeros + especiais
    total_caracteres = len(todos)

    # Simula um array fixo de caracteres da senha
    senha_array = [''] * tamanho

    # Preenche cada posição do array com um caractere aleatório
    for i in range(tamanho):
        indice = random.randint(0, total_caracteres - 1)
        senha_array[i] = todos[indice]

    # Constrói a string final a partir do array
    senha = ''
    for i in range(tamanho):
        senha += senha_array[i]

    return senha

# 19) Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. Faça um algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário.
# O percentual de aumento deve ser consultado por meio de uma função que recebe por parâmetro o cargo e retorna o percentual de aumento.
# Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber só 5% de aumento. 
# Por fim, mostre o salário antigo, o novo salário e a diferença. 


def obter_percentual(cargo):
    cargo = cargo.lower()
    if (cargo == "gerente"):
        return 0.10
    elif (cargo == "engenheiro"):
        return 0.20
    elif cargo == "técnico" or cargo == "tecnico":
        return 0.30
    else:
        return 0.05

# Entrada
salario = float(input("Digite o salário atual: R$ "))
cargo = input("Digite o cargo do funcionário: ")

# Processo
percentual = obter_percentual(cargo)
aumento = salario * percentual
novo_salario = salario + aumento

# Saída
print("\n--- Resultado ---")
print(f"Salário antigo: R$ {salario:.2f}")
print(f"Novo salário:   R$ {novo_salario:.2f}")
print(f"Reajuste:       R$ {aumento:.2f}")


# 20) Crie uma função para calcular o fatorial, mas não utilize laço de repetição e sim recursividade (função chamando ela mesmo).
def fatorial_recursiva(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * fatorial(n - 1)
    
# 21 Crie uma função soma_vetor(vetor) que recebe um vetor de números e retorna a soma de todos os elementos do vetor.
def somar_vetor(vetor):
    soma = 0
    for i in range(0, len(vetor)):
        soma += vetor[i]
    return soma
# 22) Crie uma função contar_ocorrencias(vetor, elemento) que recebe um vetor e um valor, e retorna a quantidade de vezes que o elemento aparece no vetor.

def contar_ocorrencias(vetor, elemento):
    contador = 0
    for i in range(0, len(vetor)):
        if (vetor[i] == elemento):
            contador += 1
    return contador

# 23) Crie uma função verificar_ordenacao(vetor) que recebe um vetor e retorna True se o vetor estiver em ordem crescente e False caso contrário.
def verificar_ordenacao(vetor):
    for i in range(0, len(vetor) - 1):
        if (vetor[i] > vetor[i + 1]):
            return False
    return True

# 24) Crie uma função inverter_vetor(vetor) que recebe um vetor e retorna um novo vetor com os elementos invertidos.
def inverter_vetor(vetor):
    tamanho = len(vetor)
    invertido = [0] * tamanho  # cria um vetor fixo com o mesmo tamanho

    for i in range(0, tamanho):
        invertido[i] = vetor[tamanho - 1 - i]

    return invertido

#25) Crie uma função encontrar_maior(vetor) que recebe um vetor e retorna somente o maior valor do vetor.

def encontrar_maior(vetor):
    maior = vetor[0] 
    for i in range(1, len(vetor)):
        if(vetor[i] > maior):
            maior = vetor[i]
    return maior

# 26 Crie uma função encontrar_limites(vetor) que recebe um vetor e retorna um outro vetor com somente dois valores: o menor no índice 0 e o maior no índice 1.
def encontrar_limites(vetor):
    menor = vetor[0]
    maior = vetor[0]

    for i in range(1, len(vetor)):
        if(vetor[i] < menor):
            menor = vetor[i]
        if(vetor[i] > maior):
            maior = vetor[i]
            
    vetor = [maior, menor]
    
    return vetor

# 27) Crie uma função multiplicar_vetores(vetor1, vetor2) que recebe dois vetores de igual tamanho e retorna um novo vetor com o produto dos elementos correspondentes de cada vetor.
# Exemplo:
# vetor1 = [1, 2, 3]
# vetor2 = [4, 5, 6]
# print(multiplicar_vetores(vetor1, vetor2))  # Saída esperada: [4, 10, 18]

def multiplicar_vetores(vetor1, vetor2):
    if (len(vetor1) != len(vetor2)):
        print("Erro: Vetores de tamanhos diferentes!")
        return None 

    tamanho = len(vetor1)
    resultado = [0] * tamanho

    for i in range(tamanho):
        resultado[i] = vetor1[i] * vetor2[i]

    return resultado

