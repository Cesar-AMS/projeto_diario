import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

class TratamentoDados:
    def __init__(self, texto: str):
        """
        Inicializa a instância da classe.

        Args:
        texto (str): O texto a ser processado.
        """
        self.texto = texto

        # Downloads dos recursos necessários (somente na primeira execução)
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')

    @staticmethod
    def limpar_texto(texto: str) -> str:
        """
        Limpa o texto removendo caracteres especiais, pontuações, etc.

        Returns:
        str: O texto limpo.
        """
        texto_limpo = re.sub(r'[^a-zA-Z\s]', '', texto)
        return texto_limpo

    @staticmethod
    def tokenizacao(texto: str) -> list:
        """
        Divide o texto em tokens (palavras ou partes significativas).

        Returns:
        list: Lista de tokens.
        """
        tokens = nltk.word_tokenize(texto)
        return tokens

    @staticmethod
    def remover_stopwords(tokens: list) -> list:
        """
        Remove palavras comuns que geralmente não contribuem significativamente.

        Args:
        tokens (list): Lista de tokens.

        Returns:
        list: Lista de tokens sem stopwords.
        """
        stopwords_lista = set(stopwords.words('portuguese'))
        tokens_sem_stopwords = [token for token in tokens if token.lower() not in stopwords_lista]
        return tokens_sem_stopwords

    @staticmethod
    def lemmatization(tokens: list) -> list:
        """
        Reduz as palavras à sua forma base (lemmatização).

        Args:
        tokens (list): Lista de tokens.

        Returns:
        list: Lista de tokens lematizados.
        """
        lemmatizer = WordNetLemmatizer()
        tokens_lemmatizados = [lemmatizer.lemmatize(token) for token in tokens]
        return tokens_lemmatizados

    @staticmethod
    def vetorizacao_tfidf(tokens: list) -> list:
        """
        Converte os tokens em uma representação vetorial usando TF-IDF.

        Args:
        tokens (list): Lista de tokens.

        Returns:
        list: Vetor TF-IDF.
        """
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform([" ".join(tokens)])
        return tfidf_matrix.toarray().tolist()

    def preprocessamento_completo(self) -> list:
        """
        Realiza o pré-processamento completo do texto.

        Returns:
        list: Lista de tokens após o pré-processamento.
        """
        texto_limpo = self.limpar_texto(self.texto)
        tokens = self.tokenizacao(texto_limpo)
        tokens_sem_stopwords = self.remover_stopwords(tokens)
        tokens_lemmatizados = self.lemmatization(tokens_sem_stopwords)
        vetorizado = self.vetorizacao_tfidf(tokens_lemmatizados)
        return vetorizado


