import matplotlib.pyplot as plt


valores_x = list(range(1, 5001))
valores_y = [x**3 for x in valores_x]

plt.scatter(valores_x, valores_y, c=valores_y, cmap=plt.cm.Purples, edgecolor='none', s=40)

# Define o título do gráfico e nomeia os eixos
plt.title("Números Cúbicos", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Cubo do Valor", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 5100, 0, 125100000])

plt.show()

# Arg1 — Nomeia o arquivo para a imagem do gráfico que será salva no mesmo diretório de scatter_cubos.py
# Arg2 — Remove espaços em branco extras do gráfico
# plt.savefig('cubos_plot.png', bbox_inches='tight')
