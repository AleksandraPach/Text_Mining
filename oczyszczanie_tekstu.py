import re
from nltk.corpus import stopwords

text: str = "<div><h2>It’s wonderful to </h2> <p> see 2America’s matchless<b> museums</b> <a href=""> back</a></p" \
            "></div> in the swing of things after the            past two fearful, pinched and stuttering years. " \
            "There are so many 4exhibitions opening across the 52 country, covering the gamut of     art-making, " \
            "from photographs, sculpture and weaving to drawings, the history of cinema, automobiles ;(and even the  " \
            "very niche category :) of paintings on 1 stone. Most :> of these shows have been years in the planning. " \
            "The expertise, scholarship and logistics behind every one of them would 999              astound you " \
            "even in ordinary times. It’s all the more impressive given the :( impediments, uncertainty and " \
            "heartbreak so many curators and their 2 colleagues have had to negotiate in ;> recent times. Hats off to "\
            "museum workers! "

stop_words = stopwords.words("english")


def oczyszczanie(tekst: str):
    emoji = re.findall('([;:]+[()><-]+)', tekst)
    tekst = re.sub('([;:]+[()><-]+)', '', tekst)
    tekst = tekst.lower()
    tekst = re.sub(r'\d', '', tekst)
    tekst = re.sub('<[^>]+>', '', tekst)
    tekst = re.sub(r'[^\w\s]+', '', tekst)
    tekst = re.sub(r'\s{2,}', '', tekst)
    new_tekst = (tekst + " ".join(emoji))
    return new_tekst


def zbedne_slowa(tekst: str):
    lista: list = []
    list_tekst = tekst.split(' ')
    for word in list_tekst:
        if word not in stop_words:
            lista.append(word)
    newest_tekst = (" ".join(lista))
    print(newest_tekst)


print(oczyszczanie(text))
oczyszczony_tekst = oczyszczanie(text)
zbedne_slowa(oczyszczony_tekst)
