import re
import random


def get_text(fname):
    a = r'".+"'
    with open(fname, encoding='utf-8') as inf:
        text = inf.read()

    res = re.findall(a, text)
    return [x.replace('"', '') for x in res]


def add_brat(lst):

    result = []

    for phrase in lst:
        phrase = phrase.split()
        ln = len(phrase)
        ind = random.randint(0, ln)

        if ind == 0:
            phrase[0] = phrase[0].lower()
            brat = 'Брат,'

        elif phrase[ind - 1][-1] == ',':
            phrase[ind-1].rstrip(',')
            brat = 'брат,'

        elif ind == ln:
            phrase[-1] = phrase[-1].rstrip('?').rstrip('!').rstrip('.')
            phrase[ind - 1] = phrase[ind - 1] + ','
            brat = 'брат!!!'

        else:
            phrase[ind - 1] = phrase[ind - 1] + ','
            brat = 'брат,'

        phrase.insert(ind, brat)
        phrase = ' '.join(phrase)
        result.append(phrase)

    return result
