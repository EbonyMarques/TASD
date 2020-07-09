from sklearn.feature_extraction.text import CountVectorizer as cv
from sklearn.feature_extraction.text import TfidfVectorizer as tv

class Vetorizador():
    def __init__(self):
        self.vetorizador = None
        self.revisoes = None
        self.revisoes_processadas = None

    def vetorizar_texto(self, texto):
        return self.vetorizador.transform([texto.lower().replace("'", "")])
    
    def vetorizar(self):
        self.revisoes_processadas = self.vetorizador.fit_transform(self.revisoes)

class CountVectorizer(Vetorizador):
    def __init__(self, revisoes, ngram_range = (1, 1)):
        self.vetorizador = cv(ngram_range=ngram_range)
        self.revisoes = revisoes
        self.vetorizar()
        print("\nCountVectorizer terminou a vetorização com ngram_range de %s."%str(ngram_range))

class TFIDFVectorizer(Vetorizador):
    def __init__(self, revisoes, ngram_range = (1, 1)):
        self.vetorizador = tv(ngram_range=ngram_range)
        self.revisoes = revisoes
        self.vetorizar()
        print("\nTFIDFVectorizer terminou a vetorização com ngram_range de %s."%str(ngram_range))