import unittest

from libmorris           import register_game
from libmorris           import destroy_game
from libmorris.libmorris import game_registry

class TestGameDestruction(unittest.TestCase):
  def setUp(self):
    self.game_name = 'Test Game'
    register_game(self.game_name)

  def tearDown(self):
    if self.game_name in game_registry:
      del game_registry[self.game_name]

  def test_destruction(self):
    result = destroy_game(self.game_name)

    self.assertTrue(self.game_name not in game_registry)
    self.assertTrue(result)

  def test_destruction_of_bad_name(self):
    self.assertFalse(destroy_game('wat'))
