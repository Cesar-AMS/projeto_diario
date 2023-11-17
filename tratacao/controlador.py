# tratamento/controlador.py
from typing import List

from limpar_texto import LimparTexto
from lematizacao import Lematizacao
from stop_words import RemoverStopWords
from tokenizacao import Tokenizacao
from vetorizacao import Vetorizacao

class ControladorPreprocessamento:
    def __init__(self):
        self.limpar_texto = LimparTexto()
        self.lematizacao = Lematizacao()
        self.remover_stopwords = RemoverStopWords()
        self.tokenizacao = Tokenizacao()
        self.vetorizacao = Vetorizacao()

    def preprocessar(self, texto: str) -> List[List[float]]:
        # Limpar o texto
        texto_limpo = self.limpar_texto.limpar(texto)

        # Tokenização
        tokens = self.tokenizacao.tokenizar(texto_limpo)

        # Remover Stop Words
        tokens_sem_stopwords = self.remover_stopwords.remover_stopwords(tokens)

        # Lematização
        tokens_lematizados = self.lematizacao.lematizar(tokens_sem_stopwords)

        # Vetorização TF-IDF
        vetorizado = self.vetorizacao.vetorizar_tfidf(tokens_lematizados)

        return vetorizado
