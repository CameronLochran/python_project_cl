class Spendings:
    def __init__(self, name, id = None):
        self.name = name
        self.id = id

    def tesco_sales(self, item, price, wallet):
        self.item = item
        self.price = price
        self.wallet -= wallet
        self.balance = wallet - price

    def amazon_sales(self, item, price, wallet):
        self.item = item
        self.price = price
        self.wallet -= wallet

    def scotrail_sales(self, ticket, price, wallet):
        self.ticket = ticket
        self.price = price
        self.wallet -= wallet

    def sufficient_funds(self, item):
        return self.wallet >= item.price