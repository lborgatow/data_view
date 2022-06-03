from random import choice


class PasseioAleatorio:
    """Uma classe para gerar passeios aleatórios"""

    def __init__(self, num_pontos=5000):
        """Inicializa os atributos de um passeio"""

        self.num_pontos = num_pontos

        # Todos os passeios começam em (0, 0)
        self.valores_x = [0]
        self.valores_y = [0]

    def obter_passo(self):
        """Determina a direção a ser seguida e a distância a
        ser percorrida nessa direção"""

        direcao = choice([1, -1])
        distancia = choice(list(range(5)))
        passo = direcao * distancia

        return passo

    def preencher_passeio(self):
        """Calcula todos os pontos do passeio"""

        # Continua dando passos até que o passeio alcance o tamanho desejado
        while len(self.valores_x) < self.num_pontos:

            passo_x = self.obter_passo()
            passo_y = self.obter_passo()

            # Rejeita movimentos que não vão a lugar nenhum
            if passo_x == 0 and passo_y == 0:
                continue

            # Calcula os próximos valores de x e de y
            proximo_x = self.valores_x[-1] + passo_x
            proximo_y = self.valores_y[-1] + passo_y

            self.valores_x.append(proximo_x)
            self.valores_y.append(proximo_y)
