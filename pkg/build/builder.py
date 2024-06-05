class Card():
    def __init__(self, name, mana, cardType):
        name = self.name
        mana = self.mana
        cardType = self.cardType


n = ""
m = ""
t = ""


def Build():
    return Card(n, m, t)


def Name(i):
    global n
    n = i


def Mana(i):
    global m
    m = i


def Type(i):
    global t
    t = i
