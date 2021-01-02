sundae = " "
gelato = " "
frozenYogurt = " "
softServe = " "
regular = " "
totalPrice = 0.00

print()
print("Welcome to Cherry on Top! What would you like?")
print("     Menu")
print("-------------")
print("Sundae")
print("Gelato")
print("Frozen Yogurt")
print("Soft Serve")
print("Regular")
print("-------------")

iceCreamType = input()
print()
if iceCreamType.lower() == "sundae":
    print("What sundae flavor would you like?")
    print("        Sundae Menu        ")
    print("---------------------------")
    print("Banana Split          $8.00")
    print("American Parfait      $7.50")
    print("Hot Fudge             $7.50")
    print("Peppermint Brownie    $7.80")
    print("Cookie Monster        $7.80")
    print("---------------------------")
    sundae = input()
    if sundae.lower() == "banana split":
        totalPrice = totalPrice + 8.00
    if sundae.lower() == "american parfait":
        totalPrice = totalPrice + 7.50
    if sundae.lower() == "hot fudge":
        totalPrice = totalPrice + 7.50
    if sundae.lower() == "peppermint brownie":
        totalPrice = totalPrice + 7.80
    if sundae.lower() == "cookie monster":
        totalPrice = totalPrice + 7.80
    print()

if iceCreamType.lower() == "gelato":
    print("What gelato flavor would you like?")
    print("    Gelato Menu    ")
    print("-------------------")
    print("Vanilla       $6.50")
    print("Chocolate     $6.50")
    print("Pistachio     $6.00")
    print("Custard       $6.50")
    print("Strawberry    $6.00")
    print("-------------------")
    gelato = input()

    if gelato.lower() == "vanilla":
        totalPrice = totalPrice + 6.50
    if gelato.lower() == "chocolate":
        totalPrice = totalPrice + 6.50
    if gelato.lower() == "pistachio":
        totalPrice = totalPrice + 6.00
    if gelato.lower() == "custard":
        totalPrice = totalPrice + 6.50
    if gelato.lower() == "strawberry":
        totalPrice = totalPrice + 6.00
    print()

if iceCreamType.lower() == "frozen yogurt":
    print("What frozen yogurt flavor would you like?")
    print("Frozen Yogurt Menu")
    print("------------------")
    print("Vanilla      $4.00")
    print("Chocolate    $4.00")
    print("Mint         $4.50")
    print("Coffee       $4.50")
    print("Strawberry   $4.50")
    print("------------------")
    frozenYogurt = input()
    if frozenYogurt.lower() == "vanilla":
        totalPrice = totalPrice + 4.00
    if frozenYogurt.lower() == "chocolate":
        totalPrice = totalPrice + 4.00
    if frozenYogurt.lower() == "mint":
        totalPrice = totalPrice + 4.50
    if frozenYogurt.lower() == "coffee":
        totalPrice = totalPrice + 4.50
    if frozenYogurt.lower() == "strawberry":
        totalPrice = totalPrice + 4.50
    print()

if iceCreamType.lower() == "regular":
    print("What ice cream flavor would you like?")
    print("  Ice Cream Menu  ")
    print("------------------")
    print("Vanilla      $5.00")
    print("Chocolate    $5.00")
    print("Mint         $5.50")
    print("Coffee       $5.50")
    print("Strawberry   $5.50")
    print("------------------")
    regular = input()
    if regular.lower() == "vanilla":
        totalPrice = totalPrice + 5.00
    if regular.lower() == "chocolate":
        totalPrice = totalPrice + 5.00
    if regular.lower() == "mint":
        totalPrice = totalPrice + 5.50
    if regular.lower() == "coffee":
        totalPrice = totalPrice + 5.50
    if regular.lower() == "strawberry":
        totalPrice = totalPrice + 5.50
    print()


if iceCreamType.lower() == "soft serve":
    print("What soft serve flavor would you like?")
    print("  Soft Serve Menu  ")
    print("-------------------")
    print("Vanilla       $5.20")
    print("Chocolate     $5.20")
    print("Mint          $5.70")
    print("Coffee        $5.70")
    print("Strawberry    $5.70")
    print("-------------------")
    softServe = input()
    if softServe.lower() == "vanilla":
        totalPrice = totalPrice + 5.20
    if softServe.lower() == "chocolate":
        totalPrice = totalPrice + 5.20
    if softServe.lower() == "mint":
        totalPrice = totalPrice + 5.70
    if softServe.lower() == "coffee":
        totalPrice = totalPrice + 5.70
    if softServe.lower() == "strawberry":
        totalPrice = totalPrice + 5.70
    print()
print("What size would you like?")
print("      Sizes     ")
print("----------------")
print("1 Scoop   +$1.00")
print("2 Scoops  +$2.00")
print("3 Scoops  +$3.00")
print("----------------")
size = input()
if size.lower() == "1 scoop":
    totalPrice = totalPrice + 1.00
if size.lower() == "2 scoops":
    totalPrice = totalPrice + 2.00
if size.lower() == "3 scoops":
    totalPrice = totalPrice + 3.00
print()

print("Would you like your treat to be served in a bowl or waffle cone?")
print("         Cup        ")
print("--------------------")
print("Bowl          +$1.00")
print("Waffle Cone   +$1.50")
print("--------------------")
cup = input()
if cup.lower() == "bowl":
    totalPrice = totalPrice + 1.00
if cup.lower() == "waffle cone":
    totalPrice = totalPrice + 1.50
print()


print("Would you like toppings?")
YN = input()
print()

if YN.lower() == "yes":
    print("       Toppings       ")
    print("----------------------")
    print("Cherry            FREE")
    print("Sprinkles        $0.20")
    print("Chocolate Chips  $0.40")
    print("M&Ms             $0.30")
    print("Chocolate Syrup  $0.20")
    print("----------------------")
    topping = input()

    if topping.lower() == "sprinkles":
        totalPrice = totalPrice + 0.20
    if topping.lower() == "chocolate chips":
        totalPrice = totalPrice + 0.40
    if topping.lower() == "m&ms":
        totalPrice = totalPrice + 0.30
    if topping.lower() == "chocolate syrup":
        totalPrice = totalPrice + 0.20
    print()

print("Receipt")
print("-------------")
print("Your Order: ") 
print(size,"of",end= " ")

if iceCreamType.lower() == "sundae":
    print(sundae, end= " ")
if iceCreamType.lower() == "gelato":
    print(gelato, end= " ")
if iceCreamType.lower() == "frozen yogurt":
    print(frozenYogurt, end= " ")
if iceCreamType.lower() == "soft serve":
    print(softServe, end= " ")
if iceCreamType.lower() == "regular":
    print(regular, end= " ")

print(iceCreamType)
if YN == "yes": 
    print("with",topping)

formatFloat = "${:.2f}".format(totalPrice)
print("Total:",formatFloat)
print("Thank you, have a great day!")
print("-------------")