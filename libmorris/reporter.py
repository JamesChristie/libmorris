from libmorris.win_detector import WinDetector

class Reporter:
  def __init__(self, game):
    self.game          = game
    self.win_detector  = WinDetector(self.game.game_space)
    self.winning_moves = self.win_detector.winning_positions()

  def is_in_progress(self):
    return not self.is_over()

  def is_over(self):
    return self.get_winner() and self.winning_moves

  def last_player(self):
    self.game.get_last_player()

  def next_player(self):
    self.game.opponent(self.last_player)

  def get_winner(self):
    return self.win_detector.winning_player()

  def get_current_board(self):
    pass
