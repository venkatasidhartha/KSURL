from uuid import uuid4
from urllib.parse import urlunparse
from django.conf import settings
from url_shortner.models import Urls
from url_shortner.response.createurl import CreateUrlResponse

class UrlService:

    def read(self,uuid):
        doc = Urls.objects.get(uuid=uuid)
        url = doc.url
        if not url.startswith(('https://')):
            url = 'https://' + url
        return url

    def __mapShortUrl(self,uuid):
        schema = "https"
        host_domain = settings.HOSTDOMAIN
        path = uuid
        url = urlunparse((schema,host_domain,path,'','',''))
        return url

    def create(self,url):
        uuid = str(uuid4())
        doc = Urls.objects.create(url=url,uuid=uuid)
        doc.save()

        short_url = self.__mapShortUrl(doc.uuid)
        response = CreateUrlResponse()
        response.set_short_url(short_url)
        return response

