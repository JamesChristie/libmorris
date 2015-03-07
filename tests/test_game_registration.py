import unittest

from uuid import uuid4

from libmorris      import register_game
from libmorris      import game_exists
from libmorris      import libmorris
from libmorris.game import Game

from libmorris.libmorris      import find_game
from libmorris.backend.memory import Memory

class TestGameRegistration(unittest.TestCase):
  def setUp(self):
    self.game_name  = 'Some Game'
    self.name_one   = 'Red'
    self.router_one = lambda x: x
    self.name_two   = 'Blue'
    self.router_two = lambda x: x

    self.game_id = register_game(
      game_name         = self.game_name,
      player_one_name   = self.name_one,
      player_one_router = self.router_one,
      player_two_name   = self.name_two,
      player_two_router = self.router_two
    )


  def tearDown(self):
    libmorris.persistence = Memory()

  def test_game_exists(self):
    self.assertTrue(game_exists(self.game_id))

  def test_find_game(self):
    game = find_game(self.game_id)
    self.assertTrue(isinstance(game, Game))
