

class SignupResponse:
    name = None
    email = None
    user_id = None

    def get_obj(self):
        return {key: value for key, value in vars(self).items() if value is not None}

    def set_name(self,name):
        self.name = name
    def set_email(self,email):
        self.email = email
    def set_user_id(self,user_id):
        self.user_id = user_id
    