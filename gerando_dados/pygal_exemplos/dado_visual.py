import pygal
from dado import Dado


# Cria um D6
dado = Dado()

# Faz alguns lançamentos e armazena os resultados em uma lista
resultados = [dado.rolar() for num_rolamento in range(1000)]

# Analisa os resultados
frequencias = [resultados.count(valor) for valor in range(1, dado.num_lados + 1)]

# Visualiza os resultados
hist = pygal.Bar()  # hist --> histograma

# Rótulos
hist.title = "Resultados ao rolar um D6 1000 vezes"
hist.x_labels = [str(x) for x in range(1, dado.num_lados + 1)]
hist.x_title = "Resultado"
hist.y_title = "Frequência do Resultado"

# Acrescenta uma série de valores ao gráfico
hist.add('D6', frequencias)

# Renderiza o gráfico
hist.render_to_file('dado_visual.svg')
