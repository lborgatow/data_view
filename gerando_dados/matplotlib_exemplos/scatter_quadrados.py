import matplotlib.pyplot as plt


valores_x = list(range(1, 1001))
valores_y = [x**2 for x in valores_x]

plt.scatter(valores_x, valores_y, c=valores_y, cmap=plt.cm.Purples, edgecolor='none', s=40)

# Define o título do gráfico e nomeia os eixos
plt.title("Números Quadrados", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Quadrado do Valor", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

plt.show()

# Arg1 — Nomeia o arquivo para a imagem do gráfico que será salva no mesmo diretório de scatter_quadrados.py
# Arg2 — Remove espaços em branco extras do gráfico
# plt.savefig('quadrados_plot.png', bbox_inches='tight')
