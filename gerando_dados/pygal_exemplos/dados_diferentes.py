import pygal
from dado import Dado


# Cria um dado D6 e um D10
dado_1 = Dado()
dado_2 = Dado(10)

# Faz alguns lançamentos e armazena os resultados em uma lista
resultados = [dado_1.rolar() + dado_2.rolar() for num_rolamento in range(50000)]

# Analisa os resultados
resultado_max = dado_1.num_lados + dado_2.num_lados
frequencias = [resultados.count(valor) for valor in range(2, resultado_max + 1)]

# Visualiza os resultados
hist = pygal.Bar()  # hist --> histograma

# Rótulos
hist.title = "Resultados ao rolar um dado D6 e um D10 50,000 vezes"
hist.x_labels = [str(x) for x in range(2, resultado_max + 1)]
hist.x_title = "Resultado"
hist.y_title = "Frequência do Resultado"

# Acrescenta uma série de valores ao gráfico
hist.add('D6 + D10', frequencias)

# Renderiza o gráfico
hist.render_to_file('dados_diferentes.svg')
