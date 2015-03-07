class Player:
  def __init__(self, name, move_generator=None):
    self.name           = name
    self.move_generator = move_generator

  def get_move(self, reporter):
    self.move_generator(reporter)
