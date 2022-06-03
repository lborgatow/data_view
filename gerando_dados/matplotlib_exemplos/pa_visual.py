import matplotlib.pyplot as plt
from passeio_aleatorio import PasseioAleatorio


# Continua criando novos passeios enquanto o programa estiver ativo
while True:

    # Cria um passeio aleatório e plota os pontos
    pa = PasseioAleatorio(50000)
    pa.preencher_passeio()

    # Define o tamanho da janela de plotagem
    plt.figure(dpi=77.23, figsize=(10, 6))

    # Plota os pontos e mostra o gráfico
    numero_de_pontos = list(range(pa.num_pontos))
    plt.scatter(pa.valores_x, pa.valores_y, c=numero_de_pontos, cmap=plt.cm.Purples, edgecolor='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(pa.valores_x[-1], pa.valores_y[-1], c='red', edgecolors='none', s=50)

    # Remove os eixos
    plt.xticks([])
    plt.yticks([])

    # plt.axis('off') --> "Desliga" os eixos e as bordas

    plt.show()

    continuar_executando = input("Criar outro passeio? (s/n): ")
    while continuar_executando not in 'NnSs':
        print("Resposta inválida!")
        continuar_executando = input("Criar outro passeio? (s/n): ")
    if continuar_executando in 'Nn':
        break
    if continuar_executando in 'Ss':
        continue
