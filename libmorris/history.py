class History:
  def __init__(self):
    self.move_list     = {}
    self.current_move  = 1

  def append(self, player, position):
    new_move = self.build_move(player, position)

    if self.current_move <= self.move_count():
      self.rewrite(new_move)

    self.move_list[self.current_move] = new_move
    self.current_move += 1

  def increment(self):
    self.current_move += 1

  def decrement(self):
    self.current_move -= 1

  def get_move(self, turn_number):
    return self.move_list.get(
      turn_number, None
    )

  def last_move(self):
    return self.get_move(self.current_move - 1)

  def move_count(self):
    return len(self.move_list)

  def build_move(self, player, position):
    return {
      'player':   player,
      'position': position
    }

  def rewrite(self, new_move):
    self.move_list = dict(
      (k, v) for (k, v) in self.move_list.items() if k < self.current_move
    )
