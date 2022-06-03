import json
from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle, RotateStyle
from codigos_paises import obter_codigo_pais


# Carrega os dados em uma lista
filename = 'pib_mundial.json'
with open(filename) as f_in:
    pib_data = json.load(f_in)

    # Constrói um dicionário com dados das populações
    cp_pibs = {}
    for pib_dict in pib_data:
        if pib_dict['Year'] == '2014':
            nome_pais = pib_dict['Country Name']
            pib = int(float(pib_dict['Value']))
            codigo = obter_codigo_pais(nome_pais)
            if codigo:
                cp_pibs[codigo] = pib

# Agrupa os países em três níveis de PIB
cp_pibs_1, cp_pibs_2, cp_pibs_3 = {}, {}, {}

for cp, _pib in cp_pibs.items():
    if _pib < 100000000000:
        cp_pibs_1[cp] = _pib
    elif _pib < 1000000000000:
        cp_pibs_2[cp] = _pib
    else:
        cp_pibs_3[cp] = _pib

# Vê quantos países estão em cada nível
print(len(cp_pibs_1), len(cp_pibs_2), len(cp_pibs_3))

# mm --> Mapa Mundi
mm_estilo = RotateStyle('#336699', base_style=LightColorizedStyle)
mm = World(style=mm_estilo)
mm.title = 'PIB Mundial em 2014, por País'
mm.add('0-100b', cp_pibs_1)
mm.add('100b-1t', cp_pibs_2)
mm.add('>1t', cp_pibs_3)
mm.render_to_file('pib_mundial.svg')
