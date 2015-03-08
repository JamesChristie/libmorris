from libmorris.ai.perfect import get_perfect_move

class Player:
  def __init__(self, game=None, move_procedure=None):
    self.game           = game
    self.move_procedure = move_procedure

  def get_move(self):
    if self.move_procedure:
      return self.move_procedure(self.game)
    else:
      return get_perfect_move(self, self.game)
