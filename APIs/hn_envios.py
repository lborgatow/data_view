import requests
from operator import itemgetter


# Faz uma chamada de API e armazena a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Código de status:", r.status_code)

# Processa informações sobre cada artigo submetido
ids_de_envio = r.json()
envio_dicts = []
for id_de_envio in ids_de_envio[:30]:

    # Cria uma chamada de API separada para cada artigo submetido
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(id_de_envio) + '.json')
    r_envio = requests.get(url)
    print(r_envio.status_code)
    resposta_dict = r_envio.json()
    envio_dict = {
        'titulo': resposta_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(id_de_envio),
        'comentarios': resposta_dict.get('descendants', 0)
    }
    envio_dicts.append(envio_dict)

envio_dicts = sorted(envio_dicts, key=itemgetter('comentarios'), reverse=True)
for envio_dict in envio_dicts:
    print("\nTítulo:", envio_dict['titulo'])
    print("Link de discussão:", envio_dict['link'])
    print("Comentários:", envio_dict['comentarios'])