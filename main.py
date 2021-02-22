class Credit_card:
    card_size = "default"
    __bank = None
    __user_name = None
    __numbers = None
    __cvv = None
    __card_type = None
    __currency = None


    def __init__(self, bank = None, user_name = None, numbers = None, cvv = None, card_type = None, currency = None):
        self.__bank = bank
        self.__user_name = user_name
        self.__numbers = numbers
        self.__cvv = cvv
        self.__card_type = card_type
        self.__currency = currency


    def __del__(self):
        return

    def __str__(self):
        return f"Bank: {self.__bank}\n" \
               f"User name: {self.__user_name}\n" \
               f"Numbers: {self.__numbers}\n" \
               f"CVV: {self.__cvv}\n" \
               f"Card type: {self.__card_type}\n" \
               f"Currency: {self.__currency}"

    @staticmethod
    def get_card_size():
        return Credit_card.card_size


def main():
    card_1 = Credit_card("Privat24", "ZenoviiVeres", "1337228322777666", "777", "Wood", "Shekeli")
    card_2 = Credit_card("Privat24", "ZenoviiVeres", "Shekeli")
    card_3 = Credit_card()
    print(card_1)


if __name__ == '__main__':
    main()