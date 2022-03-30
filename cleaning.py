import re
from nltk import PorterStemmer
from nltk.corpus import stopwords


def text_prepering(tekst: str) -> str:
    tekst = re.sub('([;:]+[()><-]+)', '', tekst)
    tekst = tekst.lower()
    tekst = re.sub(r'\d', '', tekst)
    tekst = re.sub('<[^>]+>', '', tekst)
    tekst = re.sub(r'[^\w\s]+', '', tekst)
    tekst = re.sub(r'\s{2,}', ' ', tekst)
    return tekst


def cleaning_words(tekst: list) -> list:
    stop_words = stopwords.words("english")
    lista: list = []
    for word in tekst:
        if word not in stop_words:
            lista.append(word)
    return lista


def stemming(wyrazenie: str) -> list:
    porter = PorterStemmer()
    list_tekst = wyrazenie.split(' ')
    return [porter.stem(word) for word in list_tekst]


def longer_words(lista: list) -> list:
    lista_nowa = []
    for word in lista:
        if len(word) > 3:
            lista_nowa.append(word)
    return lista_nowa


def text_tokenizer(text):
    tekst = text_prepering(text)
    tekst = stemming(tekst)
    tekst = cleaning_words(tekst)
    tekst = longer_words(tekst)
    return tekst
