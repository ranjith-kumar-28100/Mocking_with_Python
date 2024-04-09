import unittest
from unittest.mock import patch
from web_request import WebRequest


class TestWebRequest(unittest.TestCase):

    @patch("web_request.urlopen")
    # @patch("web_request.req.urlopen")
    def test_execute_with_success(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        wr = WebRequest("https://www.youtube.com")
        self.assertEqual(wr.execute(), "SUCCESS")

    @patch("web_request.urlopen")
    # @patch("web_request.req.urlopen")
    def test_execute_with_failure(self, mock_urlopen):
        mock_urlopen.return_value.status = 500
        wr = WebRequest("https://cmrkg.net")
        self.assertEqual(wr.execute(), "FAILURE")


if __name__ == "__main__":
    unittest.main()
