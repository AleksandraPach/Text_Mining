import re

text = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"


def liczby(string):
    new_text = re.sub(r'\d', '', string)
    return new_text


print(liczby(text))
