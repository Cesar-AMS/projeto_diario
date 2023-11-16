# tratamento/lematizacao.py
import nltk
from nltk.stem import WordNetLemmatizer
from typing import List

class Lematizacao:
    def __init__(self):
        nltk.download('wordnet')
        self.lemmatizer = WordNetLemmatizer()

    def lematizar(self, tokens: List[str]) -> List[str]:
        """
        Reduz as palavras à sua forma base (lemmatização).

        Args:
        tokens (list): Lista de tokens.

        Returns:
        list: Lista de tokens lematizados.
        """
        lematizados = [self.lemmatizer.lemmatize(token) for token in tokens]
        return lematizados
