import unittest

from libmorris.game         import Game
from libmorris.game_updater import GameUpdater

from libmorris.errors import InvalidMove
from libmorris.errors import MoveOutOfBounds

class TestGameUpdatingForValidMove(unittest.TestCase):
  def setUp(self):
    self.game     = Game()
    self.player   = self.game.player_one
    self.position = (1, 3)

  def test_is_over(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertFalse(self.game.is_over())

  def test_is_win_for(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertFalse(self.game.is_win_for(self.player))

  def test_is_loss_for(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertFalse(self.game.is_loss_for(self.player))

  def test_current_player(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertEqual(
      self.game.current_player,
      self.game.player_two
    )

  def test_get_last_player(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertEqual(
      self.game.last_player,
      self.player
    )

  def test_owner_of(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertEqual(
      self.game.owner_of(self.position),
      self.player
    )

class TestGameUpdatingForWinningMove(unittest.TestCase):
  def setUp(self):
    self.game     = Game()
    self.game.game_space = {
      (1, 3): None, (2, 3): self.game.player_one, (3, 3): self.game.player_one,
      (1, 2): None, (2, 2): self.game.player_two, (3, 2): self.game.player_two,
      (1, 1): None, (2, 1): None, (3, 1): None
    }

    self.player   = self.game.player_one
    self.position = (1, 3)

  def test_is_over(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertTrue(self.game.is_over())

  def test_is_win_for(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertTrue(self.game.is_win_for(self.player))

  def test_is_loss_for(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertFalse(self.game.is_loss_for(self.player))

  def test_current_player(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertIsNone(self.game.current_player)

  def test_get_last_player(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertEqual(
      self.game.last_player,
      self.player
    )

  def test_owner_of(self):
    GameUpdater.request_move(self.game, self.player, self.position)
    self.assertEqual(
      self.game.owner_of(self.position),
      self.player
    )

class TestGameUpdatingForOutOfBoundsMove(unittest.TestCase):
  def setUp(self):
    self.game     = Game()
    self.player   = self.game.player_one
    self.position = (-7, 30)

  def test_exception_raised(self):
    with self.assertRaises(MoveOutOfBounds):
      GameUpdater.request_move(self.game, self.player, self.position)

  def test_is_over(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertFalse(self.game.is_over())

  def test_is_win_for(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertFalse(self.game.is_win_for(self.player))

  def test_is_loss_for(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertFalse(self.game.is_loss_for(self.player))

  def test_current_player(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertEqual(
      self.game.current_player,
      self.player
    )

  def test_get_last_player(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertIsNone(self.game.last_player)

class TestGameUpdatingForOwnedMove(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.game_space = {
      (1, 3): self.game.player_two, (2, 3): None, (3, 3): None,
      (1, 2): None, (2, 2): None, (3, 2): None,
      (1, 1): None, (2, 1): None, (3, 1): None
    }

    self.player   = self.game.player_one
    self.position = (1, 3)

  def test_exception_raised(self):
    with self.assertRaises(InvalidMove):
      GameUpdater.request_move(self.game, self.player, self.position)

  def test_is_over(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertFalse(self.game.is_over())

  def test_is_win_for(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertFalse(self.game.is_win_for(self.player))

  def test_is_loss_for(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertFalse(self.game.is_loss_for(self.player))

  def test_current_player(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertEqual(
      self.game.current_player,
      self.player
    )

  def test_get_last_player(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertIsNone(self.game.last_player)

  def test_owner_of(self):
    try:
      GameUpdater.request_move(self.game, self.player, self.position)
    except:
      pass
    self.assertEqual(
      self.game.owner_of(self.position),
      self.game.player_two
    )
