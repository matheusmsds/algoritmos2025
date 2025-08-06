import matplotlib.pyplot as ptl

#Dados
x = [10,100,1000,10000, 100000]
python = [3, 27, 128, 867, 1180]
java = [2, 72, 451, 1420, 11879]
go = [2, 21, 145, 585, 5612]

ptl.plot(x, python, marker='o', label="Python")
ptl.plot(x, java, marker='s', label="Java")
ptl.plot(x, go, marker='v', label="Go")

# Titulos e Rotulos
ptl.title("Comparação das Linguagens Java, Python e Go")
ptl.xlabel("Quantidade de repetições")
ptl.ylabel("Tempo de execução")

# Exibição
ptl.grid(True)
ptl.legend()
ptl.show()