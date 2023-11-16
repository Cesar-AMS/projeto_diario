# tratamento/limpar_texto.py
import re

class LimparTexto:
    def __init__(self, padroes_remover=None):
        """
        Inicializa a instância da classe.

        Args:
        padroes_remover (list): Lista de padrões a serem removidos.
        """
        self.padroes_remover = padroes_remover or []

    def limpar(self, texto):
        """
        Limpa o texto removendo caracteres especiais, pontuações, etc.

        Args:
        texto (str): O texto a ser processado.

        Returns:
        str: O texto limpo.
        """
        for padrao in self.padroes_remover:
            texto = re.sub(padrao, '', texto)

        return texto
