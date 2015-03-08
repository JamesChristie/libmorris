from libmorris.errors import InvalidMove
from libmorris.errors import MoveOutOfBounds

class GameUpdater:
  @classmethod
  def request_move(self, game, player, position):
    GameUpdater(game).apply_move(player, position)

  def __init__(self, game):
    self.game = game

  def apply_move(self, player, position):
    if self.is_valid_move(player, position):
      self.game.set_owner_of(position, player)
      self.game.update_win_status()
      self.game.update_current_player()

  def is_valid_move(self, player, position):
    if not self.is_in_bounds(position):
      raise MoveOutOfBounds(position)
    elif self.is_position_taken(position):
      raise InvalidMove(position)
    elif self.player_can_move(player):
      return True

  def is_position_taken(self, position):
    return self.game.owner_of(position) != None

  def is_in_bounds(self, position):
    return all(1 <= n <= 3 for n in position)

  def player_can_move(self, player):
    return (
      self.game.current_player == player and
      self.game.is_in_progress()
    )
