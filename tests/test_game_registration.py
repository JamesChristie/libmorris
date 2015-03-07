import unittest

from uuid import uuid4

from libmorris        import register_game
from libmorris        import destroy_game
from libmorris        import game_exists
from libmorris        import libmorris
from libmorris.game   import Game
from libmorris.errors import GameExistsError

from libmorris.libmorris      import find_game
from libmorris.backend.memory import Memory

class TestGameRegistration(unittest.TestCase):
  def setUp(self):
    self.game_name  = 'Some Game'
    self.name_one   = 'Red'
    self.router_one = lambda x: x
    self.name_two   = 'Blue'
    self.router_two = lambda x: x

  def tearDown(self):
    libmorris.persistence = Memory()

  def test_simple_registration(self):
    game_id = register_game(
      game_name         = self.game_name,
      player_one_name   = self.name_one,
      player_one_router = self.router_one,
      player_two_name   = self.name_two,
      player_two_router = self.router_two
    )

    self.assertTrue(game_exists(game_id))

    game = find_game(game_id)
    self.assertTrue(isinstance(game, Game))

  def test_deletion_of_registered_game(self):
    game_id = register_game(
      game_name         = self.game_name,
      player_one_name   = self.name_one,
      player_one_router = self.router_one,
      player_two_name   = self.name_two,
      player_two_router = self.router_two
    )

    destroy_game(game_id)
    self.assertFalse(game_exists(game_id))

    game = find_game(game_id)
    self.assertIsNone(game)

  def test_deletion_of_non_existant_game(self):
    game_id = uuid4()

    destroy_game(uuid4())
    self.assertFalse(game_exists(game_id))

    game = find_game(game_id)
    self.assertIsNone(game)
