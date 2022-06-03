import requests


# Faz a chamada da API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Código de status:", r.status_code)

# Armazena a resposta da API em uma variável
resposta_dict = r.json()
print("Repositórios totais:", resposta_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = resposta_dict['items']
print("Repositórios retornados:", len(repo_dicts))
print("\nInformações selecionadas sobre cada repositório:")
for repo_dict in repo_dicts:
    print('\nNome:', repo_dict['name'])
    print('Proprietário:', repo_dict['owner']['login'])
    print('Estrelas:', repo_dict['stargazers_count'])
    print('Repositório:', repo_dict['html_url'])
    print('Criado:', repo_dict['created_at'])
    print('Atualizado:', repo_dict['updated_at'])
    print('Descrição:', repo_dict['description'])
