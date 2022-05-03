from cleaning import text_tokenizer, top_tokens, plot_table_most_important
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd

df_true = pd.read_csv('Datasets/True.csv', usecols=['title', 'text'])
df_fake = pd.read_csv('Datasets/Fake.csv', usecols=['title', 'text'])


def main():
    vectorizer_count = CountVectorizer(tokenizer=text_tokenizer)
    count_transform_true = vectorizer_count.fit_transform(df_true['title'])
    count_transform_fake = vectorizer_count.fit_transform(df_fake['title'])
    vectorizer_tfid = TfidfVectorizer(tokenizer=text_tokenizer)
    tfid_transform_true = vectorizer_tfid.fit_transform(df_true['title'])
    tfid_transform_fake = vectorizer_tfid.fit_transform(df_fake['title'])
    vectorizer_binary = CountVectorizer(tokenizer=text_tokenizer, binary=True)
    binary_transform_true = vectorizer_binary.fit_transform(df_true['title'])
    binary_transform_fake = vectorizer_binary.fit_transform(df_fake['title'])
    print(plot_table_most_important(
        top_tokens(count_transform_fake.toarray().sum(axis=0), vectorizer_count.get_feature_names_out(), 15),
        "Tokeny występujace tylko w tytułach fałszywych wiadomości"))
    print(plot_table_most_important(
        top_tokens(count_transform_true.toarray().sum(axis=0), vectorizer_count.get_feature_names_out(), 15),
        "Tokeny występujace tylko w tytułach prawdziwych wiadomości"))
    print(plot_table_most_important(
        top_tokens(tfid_transform_true.toarray().sum(axis=0), vectorizer_tfid.get_feature_names_out(), 15),
        "Kluczowe tokeny prawdziwych wiadomości na podstawie miary TF-IDF"))
    print(plot_table_most_important(
        top_tokens(binary_transform_true.toarray().sum(axis=0), vectorizer_binary.get_feature_names_out(), 15),
        "Crucial tokens based on binary weight"))


main()
