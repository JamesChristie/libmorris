from libmorris.board    import Board
from libmorris.reporter import Reporter

class Game:
  def __init__(self):#, player_one, player_two):
    # self.player_one = player_one
    # self.player_two = player_two
    self.board      = Board()
    self.reporter   = self.new_reporter()

  def request_move(self, player=None, position=None):
    pass

  def player_can_move(self, player):
    pass

  def new_reporter(self):
    return Reporter(self)
