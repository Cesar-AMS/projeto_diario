# tratamento/limpar_texto.py
import re

class LimparTexto:
    def __init__(self, padroes_remover=None, flags=re.IGNORECASE):
        """
        Inicializa a instância da classe.

        Args:
        padroes_remover (list): Lista de padrões a serem removidos.
        flags (int): Argumento opcional para a função re.sub(), por padrão é re.IGNORECASE.
        """
        # Padrões padrão: caracteres não alfanuméricos
        padroes_default = r'[^a-zA-Z0-9\s]'

        self.padroes_remover = padroes_remover or [padroes_default]
        self.flags = flags

    def limpar(self, texto):
        """
        Limpa o texto removendo caracteres especiais, pontuações, etc.

        Args:
        texto (str): O texto a ser processado.

        Returns:
        str: O texto limpo.
        """
        for padrao in self.padroes_remover:
            texto = re.sub(re.escape(padrao), '', texto, flags=self.flags)

        return texto
