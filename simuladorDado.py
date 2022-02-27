import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você deseja jogar o dado?'

    def iniciar(self):
        resposta = input(self.mensagem)

        try:
            if resposta == 'Sim' or resposta == 'S':
                self.GerarValorDoDado()
            elif resposta == 'Não' or resposta == 'N':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar Sim ou Não')
        except:
            print('Ocorreu um erro ao receber sua resposta!')
        
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.iniciar()