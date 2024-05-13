

class UserUpdateRequest:
    name = None
    password = None
    conform_password = None

    def __init__(self,data) -> None:
        if 'name' in data:
            self.name = data["name"]
        if 'password' in data:
            if data['password'] != data['conform_password']:
                raise ValueError("Password missmatch")
            self.password = data['password']
    
    def get_name(self):
        return self.name
    
    def get_password(self):
        return self.password
