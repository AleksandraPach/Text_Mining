import cleaning
from cleaning import text_tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

tekst_fake = pd.read_csv(r'Dataset/Fake.csv')


def main():
    text = " ".join(x for x in tekst_fake.title)
    tekst = cleaning.text_tokenizer(text)
    vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
    X_transform = vectorizer.fit_transform(tekst[:3])
    # print(X_transform)
    print(X_transform.toarray())


main()
