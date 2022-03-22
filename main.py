import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import cleaning

tekst_fake = pd.read_csv(r'Datasets/Fake.csv')
tekst_fake_title = " ".join(x for x in tekst_fake.title)
tekst_fake_title = cleaning.text_prepering(tekst_fake_title)
tekst_fake_title = cleaning.cleaning_words(tekst_fake_title)
tekst_fake_title = cleaning.stemming(tekst_fake_title)
bow = cleaning.bag_of_words(tekst_fake_title)
wc = WordCloud()
wc.generate_from_frequencies(bow)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file("wordcloud.png")

