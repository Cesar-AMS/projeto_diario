# tratamento/stop_words.py
import nltk
from nltk.corpus import stopwords
from typing import List

class RemoverStopWords:
    def __init__(self):
        nltk.download('stopwords')
        self.stopwords_lista = set(stopwords.words('portuguese'))

    def remover_stopwords(self, tokens: List[str]) -> List[str]:
        """
        Remove palavras comuns que geralmente não contribuem significativamente.

        Args:
        tokens (list): Lista de tokens.

        Returns:
        list: Lista de tokens sem stopwords.
        """
        tokens_sem_stopwords = [token for token in tokens if token.lower() not in self.stopwords_lista]
        return tokens_sem_stopwords
