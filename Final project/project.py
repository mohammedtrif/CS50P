import csv
import re
def main():
    while True:
        try:
            print("Welcome back to Playstation store :)")
            choose = int(input("\nPress 1 to show the offers\nPress 2 to back to your PlayStation menu\n"))
            if choose == 1:
                while True:
                    try:
                        choose1 = int(input("\nPress 1 to show available games\nPress 2 to show PlayStation Plus offers\nPress 3 to back\n"))
                        if choose1 == 1:
                            show_offers(1)

                            while True:
                                try:
                                    choose2 = int(input("\n\nPress 1 to browse the game\nPress 2 to back\n"))
                                    if choose2 == 1:
                                        result = cart_store()
                                        if result is not None:
                                            checkout(result)
                                    elif choose2 == 2:
                                        break
                                    else:
                                        print("Please enter 1 or 2")
                                except(ValueError):
                                    print("Please enter 1 or 2")

                        elif choose1 == 2:
                            show_offers(2)
                        elif choose1 == 3:
                            break
                        else:
                            print("Please enter 1,2 or 3")
                    except(ValueError):
                        print("Please enter 1,2 or 3")

            elif choose == 2:
                break
            else:
                print("Please enter 1 or 2")
        except(ValueError):
            print("Please enter 1 or 2")

def show_offers(x):
    if x == 1:
        free_games = []
        exclusives = []
        third_games = []
        with open("store.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["category"] == "playstation_plus":
                    continue
                if row["category"] == "freegames":
                    free_games.append(row["name"])
                if row["category"] == "exclusive":
                    exclusives.append([row["name"],row["price"],row["ps+ availbelty"]])
                if row["category"] == "third_game" :
                    third_games.append([row["name"],row["price"],row["ps+ availbelty"]])
        print("Free games: ")
        for free in free_games:
            print(f"*{free}")
        print()

        exulus = []

        for exlusive in exclusives:
            exulus.append(exlusive)
        print("PlayStation exclusives: ")
        for game in exulus:
            if game[2] == "included in ps+":
                print(f"{game[0]} ${game[1]} - {game[2]}")
                continue
            if game[2] == "":
                print(f"{game[0]} ${game[1]}")

        print()

        third = []

        for third_game in third_games:
            third.append(third_game)

        print("Third-Party games: ")
        for game in third:
            if game[2] == "included in ps+":
                print(f"{game[0]} ${game[1]} - {game[2]}")
                continue
            if game[2] == "":
                print(f"{game[0]} ${game[1]}")
    if x == 2 :
        sub_extra = []
        sub_essential = []
        sub_deluxe = []
        with open("store.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["category"] == "playstation_plus":
                    if "extra" in row["name"]:
                        sub_extra.append(row["price"])
                    if "essential" in row["name"] :
                        sub_essential.append(row["price"])
                    if "deluxe" in row["name"]:
                        sub_deluxe.append(row["price"])
        c,y,z = sorted(sub_extra)
        c1,y1,z1 = sorted(sub_essential)
        c2,y2,z2 = sorted(sub_deluxe)
        print(f"One month of Extra subscription: ${c}")
        print(f"Three month of Extra subscription: ${y}")
        print(f"One year of Extra subscription: ${z}")
        print()
        print(f"One month of Essential subscription: ${c1}")
        print(f"Three month of Essential subscription: ${y1}")
        print(f"One year of Essential subscription: ${z1}")
        print()
        print(f"One month of Deluxe subscription: ${c2}")
        print(f"Three month of Deluxe subscription: ${y2}")
        print(f"One year of Deluxe subscription: ${z2}")
        print()


def browse_games(name):
    games = []
    with open("store.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if not row["category"] == "playstation_plus":
                games.append([row["category"], row["name"], row["price"], row["ps+ availbelty"]])
    found = False
    for game in games:
        if str(game[1]).strip().lower() == str(name).strip().lower():
            t = game[1]
            found = True
            break

    if found:
        if game[0] == "freegames" and game[3] == "included in ps+":
            return(f"Game found:\n{t}\nFree")

        if game[3] == "included in ps+" and not game[0] == "freegames":
            return (f"Game found:\n{t}\nPrice: ${game[2]}\nPS+: {game[3]}")

        if game[3] == "":
            return (f"Game found:\n{t}\nPrice: ${game[2]}")
    else:
        raise ValueError("Game not found")




def cart_store():


    free_games = []
    games = []
    with open("store.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["category"] == "freegames":
                free_games.append(row["name"])
            if row["category"] == "third_game" or row["category"] == "exclusive":
                games.append([row["name"], row["price"]])


    cart = []
    library = []
    running = True

    while running:
        try:
            name = browse_games(name= input("What's the game you are looking for?: "))
            print(name)
            lines = str(name).splitlines()
            second_line = lines[1]
            if second_line in free_games:
                for free in free_games:
                    if free == second_line:
                        q = str(input("Do you want to get the game? (yes/no) ")).strip().lower()
                        if q == "yes":
                            library.append(second_line)
                            print("The game has been added")

                            q1 = str(input("Do you want to add another game? (yes/no)")).strip().lower()
                            if q1 == "yes":
                                break
                            elif q1 == "no":
                                running = False
                                break
                            else:
                                print("Please enter yes or no")
                        elif q == "no":
                            running = False
                            break
                        else:
                            print("Please enter yes or no")
            else:
                for game in games:
                    if second_line == game[0]:
                        q = str(input("Do you want to buy the game? (yes/no) ")).strip().lower()
                        if q == "yes":
                            cart.append([second_line, game[1]])
                            print("The game has been added")

                            q1 = str(input("Do you want to buy another game? (yes/no)")).strip().lower()
                            if q1 == "yes":
                                break
                            elif q1 == "no":
                                p = str(input("Do you Want to see your cart? (yes/no) ")).strip().lower()
                                if p == "yes":
                                    total_p = []
                                    print("Your cart: ")
                                    for item in cart:
                                        total_p.append(str(item[1]))
                                        print(f"Game: {item[0]}\nPrice: ${item[1]}")
                                    total = sum(float(price) for price in total_p)
                                    return (f"Total price: ${total}")

                                elif p == "no":
                                    running = False
                                    break
                                else:
                                    print("Please enter yes or no")
                            else:
                                print("Please enter yes or no")
                        elif q == "no":
                            print("ok")
                            return None
                        else:
                            print("Please enter yes or no")
        except ValueError:
            print("Game not found. Please try again.")




def checkout(x):
    print(x)
    print("To complete the payment process, please enter your credit card information")
    check1 = input("Card number: ")
    check2 = input("Expiration date: ")
    check3 = input("CVV: ")
    check4 = input("Cardholder name: ")

    result1_ = None
    result2_ = None
    result3_ = None

    result1 = re.search(r"^(\d{16})$", check1)

    if result1:
        result1_ = result1.group()

    result2 = re.search(r"^(0[1-9]|1[0-2])/(2[7-9]|[3-9]\d)$", check2)
    if result2:
        result2_ = result2.group()

    result3 = re.search(r"^(\d\d\d)$", check3)
    if result3:
        result3_ = result3.group()

    if result1_ and result2_ and result3_ and str(check4).strip():
        print("You have successfully purchased")

    else:
        print("Check your information")

if __name__ == "__main__":
    main()


