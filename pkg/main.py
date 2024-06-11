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


# Alternate code:

""" import replit
from functions import typewriter
from random import randint
from time import sleep
import time

from random import randint as t
import cursor

cursor.hide()

typewriter("Welcome to Card Creator!")
sleep(1)
replit.clear()

typewriter("What type of card are you creating? Magic(m) or Creature(c)?")
replit.clear()
cardtype = input("Type m or c ")

if cardtype == "m":
  typewriter("What is the name of your card? ")
  replit.clear()
  name = input("What is the name of your card? ")

  typewriter("Ok, what type of card is it? (artifact or game) ")
  replit.clear()
  Mctype = input("Ok, what type of card is it? (artifact or game) ")
  
  typewriter("Ok, how much mana does it cost? ")
  replit.clear()
  mana = input("Ok, how much mana does it cost? ")

  typewriter("Ok, what is the card number? ")
  replit.clear()
  cardnum = input("Ok, what is the card number? ")

  typewriter("Finally, what is the effect of this card? ")
  replit.clear()
  cardeffect = input("Finally, what is the effect of this card? ")

  print("Your "+ str(Mctype) + " card is called " + name.capitalize() + " and costs " + str(mana) + " mana.")
  print(name.capitalize() + " has the following effect: " + cardeffect + ",and the card number is " + str(cardnum))
elif cardtype == "c":
  typewriter("What is the name of your creature? ")
  replit.clear()
  name = input("What is the name of your creature? ")

  typewriter("Ok, what is the card number? ")
  replit.clear()
  cardnum = input("Ok, what is the card number? ")

  typewriter("Ok, how much mana does it cost to summon? ")
  replit.clear()
  mana = input("Ok, how much mana does it cost to summon? ")

  typewriter("Ok, how much health does it have? ")
  replit.clear()
  health = input("Ok, how much health does it have? ")

  typewriter("What is(are) the attack name(s)? Seperate names using commas, ex: Blast, Punch.")
  replit.clear()
  atknum = input("What is(are) the attack name(s)?")

  typewriter("Ok, how much damage per attack(s)? Seperate values using commas, ex: 70, 60, 9. ")
  replit.clear()
  atkdam = input("Ok, how much damage per attack(s)? Seperate values using commas, ex: 70, 60, 9. ")

  typewriter("Ok, how much mana per attack(s)? Seperate values using commas, ex: 70, 60, 9. ")
  replit.clear()
  atkman = input("Ok, how much mana per attack(s)? Seperate values using commas, ex: 70, 60, 9. ")

  print("Your creature card is called " + name.capitalize() + " with card num " + str(cardnum) + " and costs " + str(mana) + " mana.")
  print("It has " + str(health) + " health.")
  print("Its attacks are: " + str(atknum) + " with " + str(atkdam) + " damage and " + str(atkman) + " mana per attack.")
else: 
  print(cardtype + " is not a valid card type.")
  sleep(1)
  replit.clear()
  print("Please restart the program.")
  sleep(3)
  quit() """