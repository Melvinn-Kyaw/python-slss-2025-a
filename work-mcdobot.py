fries_reply = input("Do you want fries with your meal? ").lower().strip("!,.? ")

if fries_reply == "yes":
    print("Here is your meal with fries.")
elif fries_reply == "no":
    print("Here is your meal without fries.")
else:
    print(f"I don't understand what \"{fries_reply}\" means.")
