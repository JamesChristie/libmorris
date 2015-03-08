import itertools

from libmorris import traversal

from libmorris.player       import Player
from libmorris.win_detector import WinDetector

def tuple_list():
  return list(
    itertools.product(traversal.board_range, repeat=2)
  )

class Game:
  def __init__(self, hook_one=None, hook_two=None):
    self.player_one = Player(game=self, hook=hook_one)
    self.player_two = Player(game=self, hook=hook_two)

    self.last_player       = None
    self.current_player    = self.player_one
    self.winning_positions = None
    self.winner            = None

    self.game_space = dict(
      (tuple, None) for tuple in tuple_list()
    )

  def is_over(self):
    return self.winning_positions and self.winner

  def is_in_progress(self):
    return not self.is_over()

  def is_win_for(self, player):
    return player == self.winner

  def is_loss_for(self, player):
    return player == self.opponent(self.winner)

  def opponent(self, player):
    if player == self.player_one:
      return self.player_two
    elif player == self.player_two:
      return self.player_one

  def get_free_positions(self):
    return [
      position for position in self.game_space
      if self.game_space[position] == None
    ]

  def owner_of(self, position):
    return self.game_space[position]

  def set_owner_of(self, position, player):
    self.game_space[position] = player

  def update_current_player(self):
    self.last_player = self.current_player

    if self.is_in_progress():
      self.current_player = self.opponent(self.current_player)
    else:
      self.current_player = None

  def get_next_player(self):
    if self.is_in_progress():
      return self.opponent(self.current_player)
    else:
      return None

  def update_win_status(self):
    detector = WinDetector(self.game_space)
    self.winning_positions = detector.winning_positions()
    self.winner            = detector.winning_player()

  def get_copy(self):
    new_game = Game()

    new_game.player_one     = self.player_one
    new_game.player_two     = self.player_two
    new_game.current_player = self.current_player
    new_game.game_space     = self.game_space.copy()

    return new_game
