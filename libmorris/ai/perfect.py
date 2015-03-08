base_score = 10

def get_perfect_move(player, game):
  pass

class Perfect:
  def __init__(self, player, game, depth=0):
    self.player = player
    self.game   = game
    self.depth  = depth + 1
    self.moves  = {}

    self.generate_moves()

  def generate_moves(self):
    for position in self.game.get_free_positions():
      score = self.derive_score_for(position)
      self.moves[score] = position

  def derive_score_for(self, position):
    pass

  def score(self):
    if self.game.is_win_for(self.player):
      return 10 - self.depth
    elif self.game.is_loss_for(self.player):
      return self.depth - 10
    else:
      return 0

  def get_move(self):
    pass
    # generate scores for all moves
    #   - dict of positions keyed by scores
    # method to expose score
    # method to expose move by max or min score
