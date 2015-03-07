from libmorris.errors import InvalidMove, MoveOutOfBounds

class Board:
  def __init__(self):
    self.game_space = [[None]*3]*3

  def request_move(self, player, position):
    if self.is_valid_move(position):
      x_pos = position[0]
      y_pos = position[1]
      self.game_space[x_pos][y_pos] = player
    else:
      pass

  def owner_of(self, position):
    return self.game_space[position[0]][position[1]]

  def is_position_free(self, position):
    return self.owner_of(position) == None

  def is_position_taken(self, position):
    return not self.is_position_free(position)

  def is_in_bounds(self, position):
    return (0 <= position[0] <= 2) and (0 <= position[1] <= 2)

  def is_valid_move(self, position):
    if not self.is_in_bounds(position):
      raise MoveOutOfBounds(position)
    elif self.is_position_taken(position):
      raise InvalidMove(position)
    else:
      return True
