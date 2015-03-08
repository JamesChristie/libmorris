import unittest

from uuid import uuid4

from libmorris      import register_game
from libmorris      import destroy_game
from libmorris      import game_exists
from libmorris      import libmorris
from libmorris.game import Game

from libmorris.libmorris      import find_game
from libmorris.backend.memory import Memory

class TestGameDestructionForRegisteredGame(unittest.TestCase):
  def setUp(self):
    self.game_id = register_game()
    destroy_game(self.game_id)

  def tearDown(self):
    libmorris.persistence = Memory()

  def test_game_exists(self):
    self.assertFalse(game_exists(self.game_id))

  def test_find_game(self):
    self.assertIsNone(find_game(self.game_id))

class TestGameDestructionForUnregisteredGame(unittest.TestCase):
  def setUp(self):
    self.game_id = uuid4()
    destroy_game(self.game_id)

  def tearDown(self):
    libmorris.persistence = Memory()

  def test_deletion_of_non_existant_game_exists(self):
    self.assertFalse(game_exists(self.game_id))

  def test_deletion_of_non_existant_find_game(self):
    self.assertIsNone(find_game(self.game_id))
