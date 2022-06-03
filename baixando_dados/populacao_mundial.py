import json
from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle, RotateStyle
from codigos_paises import obter_codigo_pais


# Carrega os dados em uma lista
filename = 'population_data.json'
with open(filename) as f_in:
    pop_data = json.load(f_in)

    # Constrói um dicionário com dados das populações
    cp_populacoes = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            nome_pais = pop_dict['Country Name']
            populacao = int(float(pop_dict['Value']))
            codigo = obter_codigo_pais(nome_pais)
            if codigo:
                cp_populacoes[codigo] = populacao

# Agrupa os países em três níveis populacionais
cp_pops_1, cp_pops_2, cp_pops_3 = {}, {}, {}

for cp, pop in cp_populacoes.items():
    if pop < 10000000:
        cp_pops_1[cp] = pop
    elif pop < 1000000000:
        cp_pops_2[cp] = pop
    else:
        cp_pops_3[cp] = pop

# Vê quantos países estão em cada nível
print(len(cp_pops_1), len(cp_pops_2), len(cp_pops_3))

# mm --> Mapa Mundi
mm_estilo = RotateStyle('#336699', base_style=LightColorizedStyle)
mm = World(style=mm_estilo)
mm.title = 'População Mundial em 2010, por País'
mm.add('0-10m', cp_pops_1)
mm.add('10m-1b', cp_pops_2)
mm.add('>1b', cp_pops_3)
mm.render_to_file('populacao_mundial.svg')
