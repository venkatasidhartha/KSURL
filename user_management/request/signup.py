

class SignupRequest:
    name = None
    email = None
    password = None

    def __init__(self,data):
        if "name" not in data or data["name"] == "":
            raise Exception("name is missing")
        if "email" not in data or data["email"] == "":
            raise Exception("email is missing")
        if "password" not in data or data["password"] == "":
            raise Exception("password is missing")
        self.name = data["name"]
        self.email = data["email"]
        self.password = data["password"]

    def get_name(self):
        return self.name
    def get_email(self):
        return self.email 
    def get_password(self):
        return self.password