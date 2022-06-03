import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Obtém as datas e as temperaturas máximas e mínimas do arquivo
filename = 'death_valley_2014.csv'
with open(filename) as f_in:
    leitor = csv.reader(f_in)
    linha_cabecalho = next(leitor)

    datas, altas, baixas = [], [], []
    for linha in leitor:
        try:
            data = datetime.strptime(linha[0], "%Y-%m-%d")
            alta = int(linha[1])
            baixa = int(linha[3])

        except ValueError:
            print(data, '- Dados ausentes')

        else:
            datas.append(data)
            altas.append(alta)
            baixas.append(baixa)

# Faz a plotagem dos dados
fig = plt.figure(dpi=77.23, figsize=(10, 6))
plt.plot(datas, altas, c='red', alpha=0.5)
plt.plot(datas, baixas, c='blue', alpha=0.5)
plt.fill_between(datas, altas, baixas, facecolor='blue', alpha=0.1)

# Formata o gráfico
titulo = "Altas e baixas temperaturas diárias - 2014\nDeath Valley, CA"
plt.title(titulo, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
