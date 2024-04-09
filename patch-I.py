import urllib.request
import unittest
from unittest.mock import patch


class WebRequest:
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        print(response.status)
        if response.status == 200:
            return "SUCCESS"
        return "FAILURE"


class TestWebRequest(unittest.TestCase):
    def test_execute_with_success(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.return_value.status = 200
            wr = WebRequest("https://www.youtube.com")
            self.assertEqual(wr.execute(), "SUCCESS")

    def test_execute_with_failure(self):
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.return_value.status = 500
            wr = WebRequest("https://cmrkg.net")
            self.assertEqual(wr.execute(), "FAILURE")


# wr = WebRequest("https://www.google.com")
# print(wr.execute())

if __name__ == "__main__":
    unittest.main()
