import build.builder as build

prompt = ">>> "

def get(i):
    i = i.lower()
    match i:
        case "name":
            print("What is the name of this card?")
            return input(prompt)

def main():
    print("What type of card?\n\tMagic::0\n\tCreature::1")
    i = int(input(prompt))
    if i > 1 or i < 0:
        print("Error: Not valid option")
        main()
main()
