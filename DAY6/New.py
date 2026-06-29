class VISACARD:
    def __init__(self, holder_name, card_number):
        self.holder_name = holder_name
        self.card_number = card_number

    def display_details(self):
        print(self.holder_name)
        print(self.card_number)

    def compute_rewards(self, amount):
        reward = amount * 0.01
        print("Reward:", reward)


class hpvisacard(VISACARD):
    def compute_rewards(self, purchase_type, amount):
        reward = amount * 0.01

        if purchase_type == "fuel":
            reward += 10

        print("Reward:", reward)


card_type = input("Enter card type (visa/hpvisa): ").strip()

if card_type not in ["visa", "hpvisa"]:
    print("Invalid card type")
else:
    holder_name = input("Enter name: ")
    card_number = input("Enter card number: ")
    amount = float(input("Enter amount: "))

    if card_type == "visa":
        card = VISACARD(holder_name, card_number)
        card.display_details()
        card.compute_rewards(amount)

    else:
        purchase_type = input("Enter purchase type: ").strip()
        card = hpvisacard(holder_name, card_number)
        card.display_details()
        card.compute_rewards(purchase_type, amount)

    