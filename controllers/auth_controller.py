class AuthController:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def login(self, username, password):
        return self.auth_service.authenticate(username, password)

    def logout(self, user_id):
        return self.auth_service.logout(user_id)

    def register(self, username, password):
        return self.auth_service.register(username, password)
    def forgot_password(self, email):
        return self.auth_service.forgot_password(email)