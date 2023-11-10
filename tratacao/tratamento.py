# tratacao/tratamento.py
class TratamentoDados:
    def processar_entrada(self, entrada):
        # Lógica para processar a entrada aqui
        # Exemplo: converter para maiúsculas e adicionar uma resposta
        entrada_tratada = entrada.upper()
        resposta_tratada = f"Você disse: {entrada_tratada}"
        return {"entrada_usuario": entrada, "resposta_tratada": resposta_tratada}
