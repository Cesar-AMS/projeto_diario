# tratamento/tokenizacao.py
import nltk
from nltk.tokenize import word_tokenize
from typing import List

class Tokenizacao:
    def __init__(self):
        nltk.download('punkt')

    def tokenizar(self, texto: str) -> List[str]:
        """
        Divide o texto em tokens (palavras ou partes significativas).

        Args:
        texto (str): O texto a ser processado.

        Returns:
        list: Lista de tokens.
        """
        tokens = word_tokenize(texto)
        return tokens
