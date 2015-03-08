import unittest

from uuid import uuid4

from libmorris import register_game
from libmorris import game_exists
from libmorris import libmorris
from libmorris import get_game

from libmorris.game     import Game
from libmorris.reporter import Reporter

from libmorris.backend.memory import Memory

class TestGameRegistration(unittest.TestCase):
  def setUp(self):
    self.game_id = register_game()

  def tearDown(self):
    libmorris.persistence = Memory()

  def test_game_exists(self):
    self.assertTrue(game_exists(self.game_id))

  def test_find_game(self):
    reporter = get_game(self.game_id)
    self.assertTrue(isinstance(reporter, Reporter))
    self.assertTrue(isinstance(reporter.game, Game))
