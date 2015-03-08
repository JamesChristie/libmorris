from libmorris.ai.perfect import Perfect

from libmorris.reporter import Reporter

class Player:
  def __init__(self, game=None, hook=None):
    self.game = game
    self.hook = hook

  def get_move(self):
    if self.hook:
      return self.hook(self.get_reporter())
    else:
      return Perfect.get_perfect_move(self, self.game)

  def get_reporter(self):
    return Reporter(self.game)
