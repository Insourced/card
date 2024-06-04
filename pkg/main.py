class Card:
    def __init__(self, mana, name, ability):
        mana = self.mana
        name = self.name
        ability = self.ability

def _ask(q):
    print(q)
    i = input(">>> ")
    j = "nil"
    match i.lower():
        case "monster":
            j = "Monster"
        case "game":
            j = "Game"
    confirmString = f"You picked {j} [Y/n]"
    confirm = input(confirmString)
    if confirm.lower() == "y":
        return True, i
    if confirm.lower() == "":
        return True, i
    return False, ""

err, type = _ask("""Pick a card type:\n\tMonster::0\n\tGame::1""")
