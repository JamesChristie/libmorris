import unittest

from libmorris.player   import Player
from libmorris.game     import Game
from libmorris.reporter import Reporter

class TestReporterForEmptyGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()

    self.expected_board_representation = {
      (1, 3): None, (2, 3): None, (3, 3): None,
      (1, 2): None, (2, 2): None, (3, 2): None,
      (1, 1): None, (2, 1): None, (3, 1): None
    }

    self.reporter = Reporter(self.game)

  def test_is_in_progress(self):
    self.assertTrue(self.reporter.is_in_progress())

  def test_is_over(self):
    self.assertEqual(self.reporter.is_over(), False)

  def test_is_tie(self):
    self.assertEqual(self.reporter.is_tie(), False)

  def test_last_player(self):
    self.assertIsNone(self.reporter.last_player())

  def test_current_player(self):
    self.assertEqual(self.reporter.current_player(), 1)

  def test_next_player(self):
    self.assertEqual(self.reporter.next_player(), 2)

  def test_winner(self):
    self.assertIsNone(self.reporter.winner())

  def test_loser(self):
    self.assertIsNone(self.reporter.loser())

  def test_get_current_board(self):
    self.assertEqual(
      self.reporter.get_current_board(),
      self.expected_board_representation
    )

  def test_get_free_positions(self):
    self.assertCountEqual(
      self.reporter.get_free_positions(),
      self.game.get_free_positions()
    )

class TestReporterForInProgressGame(unittest.TestCase):
  def setUp(self):
    self.game       = Game()
    self.player_one = self.game.player_one
    self.player_two = self.game.player_two

    self.game.last_player    = self.player_one
    self.game.current_player = self.player_two

    self.game.game_space = {
      (1, 3): self.player_one, (2, 3): self.player_one, (3, 3): None,
      (1, 2): self.player_two, (2, 2): self.player_one, (3, 2): self.player_one,
      (1, 1): self.player_one, (2, 1): self.player_two, (3, 1): self.player_two
    }

    self.expected_board_representation = {
      (1, 3): 1, (2, 3): 1, (3, 3): None,
      (1, 2): 2, (2, 2): 1, (3, 2): 1,
      (1, 1): 1, (2, 1): 2, (3, 1): 2
    }

    self.reporter = Reporter(self.game)

  def test_is_in_progress(self):
    self.assertTrue(self.reporter.is_in_progress())

  def test_is_over(self):
    self.assertEqual(self.reporter.is_over(), False)

  def test_is_tie(self):
    self.assertEqual(self.reporter.is_tie(), False)

  def test_last_player(self):
    self.assertEqual(self.reporter.last_player(), 1)

  def test_current_player(self):
    self.assertEqual(self.reporter.current_player(), 2)

  def test_next_player(self):
    self.assertEqual(self.reporter.next_player(), 1)

  def test_winner(self):
    self.assertIsNone(self.reporter.winner())

  def test_loser(self):
    self.assertIsNone(self.reporter.loser())

  def test_get_current_board(self):
    self.assertEqual(
      self.reporter.get_current_board(),
      self.expected_board_representation
    )

  def test_get_free_positions(self):
    self.assertCountEqual(
      self.reporter.get_free_positions(),
      self.game.get_free_positions()
    )

class TestReporterForFinishedGame(unittest.TestCase):
  def setUp(self):
    self.game       = Game()
    self.player_one = self.game.player_one
    self.player_two = self.game.player_two

    self.game.last_player    = self.player_two
    self.game.current_player = self.player_one

    self.game.game_space = {
      (1, 3): self.player_one, (2, 3): self.player_one, (3, 3): self.player_one,
      (1, 2): self.player_two, (2, 2): self.player_one, (3, 2): self.player_one,
      (1, 1): self.player_one, (2, 1): self.player_two, (3, 1): self.player_two
    }

    self.expected_board_representation = {
      (1, 3): 1, (2, 3): 1, (3, 3): 1,
      (1, 2): 2, (2, 2): 1, (3, 2): 1,
      (1, 1): 1, (2, 1): 2, (3, 1): 2
    }

    self.reporter = Reporter(self.game)

  def test_is_in_progress(self):
    self.assertFalse(self.reporter.is_in_progress())

  def test_is_over(self):
    self.assertEqual(self.reporter.is_over(), True)

  def test_is_tie(self):
    self.assertEqual(self.reporter.is_tie(), False)

  def test_last_player(self):
    self.assertEqual(self.reporter.last_player(), 2)

  def test_current_player(self):
    self.assertEqual(self.reporter.current_player(), 1)

  def test_next_player(self):
    self.assertIsNone(self.reporter.next_player())

  def test_winner(self):
    self.assertEqual(self.reporter.winner(), 1)

  def test_loser(self):
    self.assertEqual(self.reporter.loser(), 2)

  def test_get_current_board(self):
    self.assertEqual(
      self.reporter.get_current_board(),
      self.expected_board_representation
    )

  def test_get_free_positions(self):
    self.assertCountEqual(self.reporter.get_free_positions(), [])
