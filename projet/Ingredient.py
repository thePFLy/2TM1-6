class Ingredient:
    """
    class Ingredient represents of ingredients used for a meal
    """

    def __init__(self, name , quantity, price):
        """
        this function allows you to create an ingredient object
        PRE: a str name, an int quantity and a float price
        POST: an ingredient object created

        """

        self.name = name
        self.quantity = quantity
        self.price = price

    pass
