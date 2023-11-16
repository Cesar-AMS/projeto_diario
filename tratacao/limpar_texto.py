# importaçao biblioteca
import re

# classe para limpar textos
class Limpar_texto:

    # construtor
    def __init__(self, texto: str):

        self.texto = texto

    # metodo de limpar texto
    @staticmethod
    def limpar_texto(texto: str) -> str:
        """
        Limpa o texto removendo caracteres especiais, pontuações, etc.

        Returns:
        str: O texto limpo.
        """
        texto_limpo = re.sub(r'[^a-zA-Z\s]', '', texto)
        return texto_limpo
