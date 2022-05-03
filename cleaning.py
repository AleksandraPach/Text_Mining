import re
import numpy as np
import matplotlib.pyplot as plt
from nltk import PorterStemmer
from nltk.corpus import stopwords
from prettytable import PrettyTable


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


def top_tokens(list_of_tokens, token_words, how_many) -> dict:
    sum_list = list_of_tokens
    suma = -np.sort(-sum_list)[:10]
    top_words = []
    top_counts = []
    top_dict = {}
    for i in range(how_many):
        token_index = np.argmax(list_of_tokens)
        top_words.append(token_words[token_index])
        top_counts.append(list_of_tokens[token_index])
        list_of_tokens[token_index] = 0
    for key, value in zip(top_words, top_counts):
        top_dict[key] = value
    return top_dict


def top_documents(list_of_documents, how_many) -> list:
    list_of_documents = list_of_documents
    top_list = []
    for i in range(how_many):
        token_index = np.argmax(list_of_documents, 0)
        top_list.append(token_index)
        list_of_documents[token_index] = 0
    return top_list


def plot_table_most_important(top_dict, title):
    # plot
    words = list(top_dict.keys())[::-1]
    counts = list(top_dict.values())[::-1]
    plt.subplots(figsize=(11, 5))
    y_pos = np.arange(len(words))
    plt.barh(y_pos, counts)
    plt.yticks(y_pos, words)
    plt.ylabel("Term")
    plt.xlabel("Count")
    plt.title(title)
    plt.show()
    # pretty table
    pretty_table = PrettyTable()
    pretty_table.title = title
    pretty_table.add_column("Term", words[::-1])
    pretty_table.add_column("Count", counts[::-1])
    return pretty_table
