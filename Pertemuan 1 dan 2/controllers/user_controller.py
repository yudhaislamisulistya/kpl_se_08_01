class UserController:
    def __init__(self, user_model):
        self.user_model = user_model

    def create_user(self, name: str, email: str):
        return self.user_model(name, email)