import itertools

from libmorris.errors import InvalidMove, MoveOutOfBounds

def tuple_list():
  return list(
    itertools.product(range(1, 4), repeat=2)
  )

class Board:
  def __init__(self):
    self.game_space = dict(
      (tuple, None) for tuple in tuple_list()
    )

  def request_move(self, player, position):
    if self.is_valid_move(position):
      self.game_space[position] = player

  def owner_of(self, position):
    return self.game_space[position]

  def is_position_free(self, position):
    return self.owner_of(position) == None

  def is_position_taken(self, position):
    return not self.is_position_free(position)

  def is_in_bounds(self, position):
    return all(1 <= n <= 3 for n in position)

  def is_valid_move(self, position):
    if not self.is_in_bounds(position):
      raise MoveOutOfBounds(position)
    elif self.is_position_taken(position):
      raise InvalidMove(position)
    else:
      return True
