from libmorris.game_updater import GameUpdater

class GameAdvancer:
  @classmethod
  def resolve_next_turn(self, game):
    GameAdvancer(game).update_game()

  def __init__(self, game):
    self.game      = game
    self.updater   = GameUpdater(self.game)
    self.player    = self.game.current_player
    self.next_move = self.player.get_move()

  def update_game(self):
    if self.is_valid_move():
      self.updater.apply_move(self.player, self.next_move)

  def is_valid_move(self):
    return self.updater.is_valid_move(self.player, self.next_move)
