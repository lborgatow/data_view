import pygal
from dado import Dado


# Cria dois dados D6
dado_1 = Dado()
dado_2 = Dado()

# Faz alguns lançamentos e armazena os resultados em uma lista
resultados = [dado_1.rolar() + dado_2.rolar() for num_rolamento in range(1000)]

# Analisa os resultados
resultado_max = dado_1.num_lados + dado_2.num_lados
frequencias = [resultados.count(valor) for valor in range(1, resultado_max + 1)]

# Visualiza os resultados
hist = pygal.Bar()  # hist --> histograma

# Rótulos
hist.title = "Resultados ao rolar dois dados D6 1000 vezes"
hist.x_labels = [str(x) for x in range(2, resultado_max + 1)]
hist.x_title = "Resultado"
hist.y_title = "Frequência do Resultado"

# Acrescenta uma série de valores ao gráfico
hist.add('D6 + D6', frequencias)

# Renderiza o gráfico
hist.render_to_file('dados_visual.svg')
