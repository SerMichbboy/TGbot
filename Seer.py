import random


def read():
    with open("list_phrases.txt", encoding='utf=8')as f:
        f = f.readlines()
        list_phrases = []
        for i in f:
            phrases = i.split('\n')
            list_phrases.append(phrases[0])
            final_phrase = random.choice(list_phrases)
            final_phrase = final_phrase.capitalize()
        return final_phrase


