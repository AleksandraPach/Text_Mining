from nltk.stem import PorterStemmer

text: str = "If you stand on the northernmost tip of Bird Island, it can feel like you're looking at eternity: there " \
            "is ocean as far as the eye can see. The effect is similar when you snorkel off the same shore; not far " \
            "out from the beach, the Earth plunges away into a dark oceanic abyss hundreds, then thousands, " \
            "of metres deep. The feeling is akin to vertigo."
lista: list = text.split(" ")


def normalizacja(wyrazenie: list):
    porter = PorterStemmer()
    return [porter.stem(word) for word in wyrazenie]


lista = normalizacja(lista)
print(normalizacja(lista))
