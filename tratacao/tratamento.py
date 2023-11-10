from unidecode import unidecode

class TratamentoDados:
    def processar_entrada(self, entrada):
        entrada_sem_acentos = self.remover_acentos(entrada)
        entrada_sem_espacos = self.remover_espacos(entrada_sem_acentos)

        resposta_tratada = f"Você disse: {entrada_sem_espacos}"
        return {"entrada_usuario": entrada, "resposta_tratada": resposta_tratada}

    def remover_acentos(self, texto):
        return unidecode(texto)

    def remover_espacos(self, texto):
        return texto.replace(" ", "")
