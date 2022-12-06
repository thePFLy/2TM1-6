class Ingredient:
    """
    class Ingredient represents of ingredients used for a meal
    """

    def __init__(self, name , quantity, price):
        """
        this function allows you to create an ingredient object
        PRE: name, quantity and price
        POST: an ingredient object created

        """

        self.name = name
        self.quantity = quantity
        self.price = price

    pass