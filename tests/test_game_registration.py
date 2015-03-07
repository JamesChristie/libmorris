import unittest

from libmorris           import register_game
from libmorris.libmorris import game_registry
from libmorris.game      import Game
from libmorris.errors    import GameExistsError

class TestGameRegistration(unittest.TestCase):
  def setUp(self):
    self.game_name = 'Test Game'

  def tearDown(self):
    if self.game_name in game_registry:
      del game_registry[self.game_name]

  def test_simple_registration(self):
    register_game(self.game_name)
    self.assertTrue(self.game_name in game_registry)

    game = game_registry[self.game_name]
    self.assertTrue(isinstance(game, Game))

  def test_duplicate_registration(self):
    register_game(self.game_name)

    with self.assertRaises(GameExistsError):
      register_game(self.game_name)

if __name__ == '__main__':
  unittest.main()
