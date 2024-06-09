import build.builder as build
prompt = ">>> "
def get(i):
    i = i.lower()
    match i:
        case "name":
            return getHandeler("What is the name of this card")
        case "mana":
            return getHandeler("What is the mana of this card")
        case "number":
            return getHandeler("What is number is this card")
        case "hp":
            return getHandeler("Who much health")
        case "atkname":
            return getHandeler("What is the name of this attack")
        case "damage":
            return getHandeler("How much mana does this attack cost")
        case "type":
            return getHandeler("What type is this card")
        case "effect":
            return getHandeler("What is effect does this card have")
def getHandeler(q):
    print(q)
    return input(prompt)
def magic():
    return build.MagicCard(get("name"), get("type"), get("mana"), get("number"), get("effect"))
def creature():
    return
def main():
    print("What type of card?\n\tMagic::0\n\tCreature::1")
    i = int(input(prompt))
    if i > 1 or i < 0:
        print("Error: Not valid option")
        main()
    if i == 0:
        print(magic())
main()
