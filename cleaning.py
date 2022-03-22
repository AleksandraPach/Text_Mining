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


def cleaning_words(tekst: str) -> list:
    stop_words = stopwords.words("english")
    lista: list = []
    list_tekst = tekst.split(' ')
    for word in list_tekst:
        if word not in stop_words:
            lista.append(word)
    return lista


def stemming(wyrazenie: list) -> list:
    porter = PorterStemmer()
    return [porter.stem(word) for word in wyrazenie]


def bag_of_words(words: list) -> dict:
    bow = {}
    for word in words:
        if word not in bow.keys():
            bow[word] = 1
        else:
            bow[word] += 1
    return bow
