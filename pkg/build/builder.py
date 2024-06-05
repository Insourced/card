class Card():
    def __init__(self, name, mana, cardType):
        name = self.name
        mana = self.mana
        cardType = self.cardType

def Build(name, mana, cardType):
    return Card(name, mana, cardType)
def BuildConfig(i):
    print(i)
    return input(">>> ")
