import matplotlib.pyplot as plt


valores_entrada = [1, 2, 3, 4, 5]
quadrados = [1, 4, 9, 16, 25]
plt.plot(valores_entrada, quadrados, linewidth=5)

# Define o título do gráfico e nomeia os eixos
plt.title("Números Quadrados", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Quadrado do Valor", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)

plt.show()
