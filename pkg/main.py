import build.builder as builder


prompt = ">>> "
j = ""


def _ask(i):
    global j
    i = i.lower()
    con = f"{i} [Y/n] "
    match i:
        case "type":
            print("What type is your card?\n\tMonster::0\n\tGame::1")
            j = input(prompt)
            j = int(j)
            if j == 0:
                _ask(i)
                return i
        case "name":
            print("What name is the name of your card?")
            j = input(prompt)
            if j != "":
                print("Name cannot be nil")
                return
        case "mana":
            print("How much mana will this card have?")
            j = input(prompt)
        case _:
            k = input(con)
            if k == "y" or k == "":
                return i
            return
    return j


_ask("ype")
