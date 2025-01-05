'''
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill. Use the input() function to get a user's preferences
and then add up the total for their order and tell them how much they have to pay.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1
'''

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


smallPizza = 15
mediumPizza = 20
largePizza = 25
smallPepperoni = 2
mediumOrLargePepperoni = 3
extraCheese = 1

bill = 0
if size == "S":
    bill = smallPizza
    if pepperoni == "Y":
        bill += smallPepperoni
        if extra_cheese == "Y":
            bill += extraCheese
    else:
        if extra_cheese == "Y":
            bill += extraCheese
elif size == "M":
    bill = mediumPizza
    if pepperoni == "Y":
        bill += mediumOrLargePepperoni
        if extra_cheese == "Y":
            bill += extraCheese
    else:
        if extra_cheese == "Y":
            bill += extraCheese
else:
    bill = largePizza
    if pepperoni == "Y":
        bill += mediumOrLargePepperoni
        if extra_cheese == "Y":
            bill += extraCheese
    else:
        if extra_cheese == "Y":
            bill += extraCheese
print(f"Your final bill is: ${bill}.")

