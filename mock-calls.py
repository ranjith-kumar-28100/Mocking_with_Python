import unittest
from unittest.mock import MagicMock


class MockCallsTest(unittest.TestCase):
    def test_mock_calls(self):
        mock = MagicMock()
        mock()
        mock.assert_called()

    def test_mock_not_called(self):
        mock = MagicMock()
        mock.assert_not_called()

    def test_mock_called_with(self):
        mock = MagicMock()
        mock.side_effect = lambda x, y, z: x + y + z
        print(mock(1, 2, 3))
        mock.assert_called_with(1, 2, 3)

    def test_mock_attribute(self):
        mock = MagicMock()
        mock()
        self.assertTrue(mock.called)
        mock(10)
        self.assertEqual(mock.call_count, 2)
        print(mock.mock_calls)


if __name__ == "__main__":
    unittest.main()
