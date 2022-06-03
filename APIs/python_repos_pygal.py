import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz a chamada da API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Código de status:", r.status_code)

# Armazena a resposta da API em uma variável
resposta_dict = r.json()
print("Repositórios totais:", resposta_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = resposta_dict['items']
print("Número de itens:", len(repo_dicts))
nomes, plot_dicts = [], []
for repo_dict in repo_dicts:
    nomes.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# Cria a visualização
estilo = LS('#333366', base_style=LCS)
config = pygal.Config()
config.x_label_rotation = 45
config.show_legend = False
config.title_font_size = 24
config.label_font_size = 14
config.major_label_font_size = 18
config.truncate_label = 15
config.show_y_guides = False
config.width = 1000

grafico = pygal.Bar(config, style=estilo)
grafico.title = 'Projetos Python mais Estrelados no GitHub'
grafico.x_labels = nomes
grafico.add('', plot_dicts)
grafico.render_to_file('python_repos.svg')