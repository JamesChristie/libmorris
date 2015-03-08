import unittest

from libmorris.player   import Player
from libmorris.game     import Game
from libmorris.reporter import Reporter

class TestReporterForEmptyGame(unittest.TestCase):
  def setUp(self):
    self.game       = Game()
    self.player_one = Player()
    self.player_two = Player()

    self.game.player_one = self.player_one
    self.game.player_two = self.player_two

    self.reporter = Reporter(self.game)

  def test_is_in_progress(self):
    self.assertTrue(self.reporter.is_in_progress())

  def test_is_over(self):
    self.assertFalse(self.reporter.is_over())

  def test_get_winner(self):
    self.assertIsNone(self.reporter.get_winner())

class TestReporterForInProgressGame(unittest.TestCase):
  def setUp(self):
    self.game       = Game()
    self.player_one = Player()
    self.player_two = Player()

    self.game.player_one = self.player_one
    self.game.player_two = self.player_two

    self.game.game_space = {
      (1, 3): self.player_one, (2, 3): self.player_one, (3, 3): None,
      (1, 2): self.player_two, (2, 2): self.player_one, (3, 2): self.player_one,
      (1, 1): self.player_one, (2, 1): self.player_two, (3, 1): self.player_two
    }

    self.reporter = Reporter(self.game)

  def test_is_in_progress(self):
    self.assertTrue(self.reporter.is_in_progress())

  def test_is_over(self):
    self.assertFalse(self.reporter.is_over())

  def test_get_winner(self):
    self.assertIsNone(self.reporter.get_winner())

class TestReporterForFinishedGame(unittest.TestCase):
  def setUp(self):
    self.game       = Game()
    self.player_one = Player()
    self.player_two = Player()

    self.game.player_one = self.player_one
    self.game.player_two = self.player_two

    self.game.game_space = {
      (1, 3): self.player_one, (2, 3): self.player_one, (3, 3): self.player_one,
      (1, 2): self.player_two, (2, 2): self.player_one, (3, 2): self.player_one,
      (1, 1): self.player_one, (2, 1): self.player_two, (3, 1): self.player_two
    }

    self.reporter = Reporter(self.game)

  def test_is_in_progress(self):
    self.assertFalse(self.reporter.is_in_progress())

  def test_is_over(self):
    self.assertTrue(self.reporter.is_over())

  def test_get_winner(self):
    self.assertEqual(
      self.reporter.get_winner(),
      self.player_one
    )
