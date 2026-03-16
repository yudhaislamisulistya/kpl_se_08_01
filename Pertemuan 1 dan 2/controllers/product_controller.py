class ProductController:
    def __init__(self, item_model):
        self.item_model = item_model

    def create_product(self, name: str, price: float):
        return self.item_model(name, price)