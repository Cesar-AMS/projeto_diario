# tratamento/vetorizacao.py
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List

class Vetorizacao:
    def __init__(self):
        # Pode adicionar parâmetros personalizados para o vetorizador aqui, se necessário
        self.tfidf_vectorizer = TfidfVectorizer()

    def vetorizar_tfidf(self, tokens: List[str]) -> List[List[float]]:
        """
        Converte os tokens em uma representação vetorial usando TF-IDF.

        Args:
        tokens (list): Lista de tokens.

        Returns:
        list: Vetor TF-IDF.
        """
        tfidf_matrix = self.tfidf_vectorizer.fit_transform([" ".join(tokens)])
        return tfidf_matrix.toarray().tolist()
