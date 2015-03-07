from libmorris.board  import Board
from libmorris.errors import MissingAttribute

class Game:
  def __init__(self, **kwargs):
    try:
      self.name = kwargs['name']
    except KeyError:
      raise MissingAttribute(self.__class__.__name__, 'name')

    self.player_one = kwargs['player_one']
    self.player_two = kwargs['player_two']
    self.board      = Board()
