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

    def limpar_texto(self) -> str:
        """
        Limpa o texto removendo caracteres especiais, pontuações, etc.

        Returns:
        str: O texto limpo.
        """
        texto_limpo = re.sub(r'[^a-zA-Z\s]', '', self.texto)
        return texto_limpo

    def tokenizacao(self) -> list:
        """
        Divide o texto em tokens (palavras ou partes significativas).

        Returns:
        list: Lista de tokens.
        """
        tokens = nltk.word_tokenize(self.texto)
        return tokens

    def remover_stopwords(self, tokens: list) -> list:
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

    def lemmatization(self, tokens: list) -> list:
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

    def preprocessamento_completo(self) -> list:
        """
        Realiza o pré-processamento completo do texto.

        Returns:
        list: Lista de tokens após o pré-processamento.
        """
        texto_limpo = self.limpar_texto()
        tokens = self.tokenizacao()
        tokens_sem_stopwords = self.remover_stopwords(tokens)
        tokens_lemmatizados = self.lemmatization(tokens_sem_stopwords)
        return tokens_lemmatizados

    def vetorizacao_tfidf(self, tokens: list) -> list:
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