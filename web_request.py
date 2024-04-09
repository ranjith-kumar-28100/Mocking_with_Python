from urllib.request import urlopen

# import urllib.request as req


class WebRequest:
    def __init__(self, url):
        self.url = url

    def execute(self):
        # response = req.urlopen(self.url)
        response = urlopen(self.url)
        print(response.status)
        if response.status == 200:
            return "SUCCESS"
        return "FAILURE"
