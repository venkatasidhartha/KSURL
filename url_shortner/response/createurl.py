

class CreateUrlResponse:
    short_url = None

    def get_dict(self):
        return {key: value for key, value in vars(self).items() if value is not None}
    
    def set_short_url(self,short_url):
        self.short_url = short_url
    