import unittest
from unittest.mock import MagicMock


class Actor:
    def jump_out_of_helicopter(self):
        return "Nope, not doing it"

    def light_on_fire(self):
        return "Heck no, Where's my agent"


class Movie:
    def __init__(self, actor):
        self.actor = actor

    def start_fliming(self):
        self.actor.jump_out_of_helicopter()
        self.actor.light_on_fire()


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.actor_mock = MagicMock()
        self.movie = Movie(self.actor_mock)

    def test_start_fliming(self):
        self.movie.start_fliming()
        self.actor_mock.jump_out_of_helicopter.assert_called()
        self.actor_mock.light_on_fire.assert_called()


if __name__ == "__main__":
    unittest.main()
