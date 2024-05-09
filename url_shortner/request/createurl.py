

class CreateUrlRequest:
    url = None

    def __init__(self,request_data) -> None:
        if "url" not in request_data:
            raise ValueError("url paramenter is required")
        if not request_data["url"]:
            raise ValueError("url is empty")
        self.url = request_data["url"]
    
    def get_url(self):
        return self.url
