import pandas as pd

class TratamentoDados:

    def __init__(self, dados):
        self.dados = dados

    def ler_dados(self):
        # Ler os dados de entrada
        return self.dados

    def tratar_dados(self):
    # Aplicar as operações de tratamento
        dados = self.dados.upper()
        return dados


    def retornar_dados(self):
        # Retornar os dados tratados
        return self.dados


