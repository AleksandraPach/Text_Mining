import numpy as np
import pandas as pd
from cleaning import text_tokenizer, top_tokens, top_documents
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

df = pd.read_csv('Datasets/True.csv', usecols=['title', 'text'])


def main():
    vectorizer_count = CountVectorizer(tokenizer=text_tokenizer)
    count_transform = vectorizer_count.fit_transform(df['title'])
    vectorizer_tfid = TfidfVectorizer(tokenizer=text_tokenizer)
    tfid_transform = vectorizer_tfid.fit_transform(df['title'])
    # print(count_transform.toarray()) #nie bedzie 0, tylko same 1
    print("Pytanie 1 Jeśli do vectorizera liczebnościowego przekażemy jedynie jeden dokument, to jakie "
          "wartości będzie miała otrzymana macierz? Albo jakich nie będzie miała?")
    print("Odp: Puszczajac kod, ktory jest zakomentowany poznamy odpowiedz, ze wyswietla sie same 1, "
          "zadnych 0 nie bedzie")

    top_often_tokens: list = top_tokens(count_transform.toarray().sum(axis=0),
                                        vectorizer_count.get_feature_names_out(), 10)
    print("Top 10 najczesciej wystepujacych tokenow")
    print(top_often_tokens)
    top_important_tokens: list = top_tokens(tfid_transform.toarray().sum(axis=0),
                                            vectorizer_tfid.get_feature_names_out(), 10)
    print("Top 10 najwazniejszych tokenow")
    print(top_important_tokens)
    top_often_dokuments: list = top_documents(count_transform.toarray().sum(axis=0), 10)
    print("Top 10 najczesciej wystepujacych dokumentow")
    for doc in top_often_dokuments:
        print(df['title'][doc])


if __name__ == '__main__':
    main()
