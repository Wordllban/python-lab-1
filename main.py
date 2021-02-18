class Credit_card:
    card_size = "default"

    def __init__(self, bank=None, user_name=None, numbers=None, cvv=None, card_type=None, currency=None):
        self.bank = bank
        self.user_name = user_name
        self.numbers = numbers
        self.cvv = cvv
        self.card_type = card_type
        self.currency = currency

    def __del__(self):
        return

    def __str__(self):
        return f"Bank: {self.bank}\n" \
               f"User name: {self.user_name}\n" \
               f"Numbers: {self.numbers}\n" \
               f"CVV: {self.cvv}\n" \
               f"Card type: {self.card_type}\n" \
               f"Currency: {self.currency}"

    @staticmethod
    def get_card_size():
        return Credit_card.card_size


def main():
    card_1 = Credit_card("Privat24", "Zenovii Veres", "1337228322777666", "777", "Wood", "Shekeli")
    card_2 = Credit_card("Privat24", "Zenovii Veres", "Shekeli")
    card_3 = Credit_card()
    print(card_2)


if __name__ == '__main__':
    main()