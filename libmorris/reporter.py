class Reporter:
  def __init__(self, game):
    self.game = game

  def is_in_progress(self):
    pass

  def is_over(self):
    return not self.is_in_progress()

  def last_player(self):
    pass

  def next_player(self):
    pass

  def winner(self):
    pass

  def loser(self):
    pass

  def current_board(self):
    pass
